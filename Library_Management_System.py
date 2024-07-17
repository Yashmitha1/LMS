import mysql.connector
from tabulate import tabulate

#db=input('Enter name of your database:')
mydb=mysql.connector.connect(host='localhost',user='root',password='Starkiealwaysop')
mycursor=mydb.cursor(buffered=True)
mycursor.execute('Show databases')
data1=mycursor.fetchall()
print('The existing databases are:')
print(tabulate(data1,headers=['Database Names'],tablefmt='psql'))
db=input('Enter name of the database you want to select:')
mycursor.execute("use "+db)                      #using database
print('Database',db,'selected successfully...')        
def base():                                       #defining main menu function
    print('\n\n','*'*10,'MAIN MENU','*'*10)
    print('1.SHOW EXISTING TABLES')
    print('2.BOOK KEEPING MENU')
    print('3.ISSUING/RETURNING MENU')
    print('4.EXIT')
    k=int(input('Enter your choice:'))
    #choice-output for main menu fxn starts
    if k==1:
        print()
        mycursor.execute('show tables')
        data=mycursor.fetchall()
        for i in data:
            for j in i:
                mycursor.execute('select * from '+j)
                data=mycursor.fetchall()
                l=[]
                for k in mycursor.description:
                    l.append(k[0])
                print('Table:',j)
                print(tabulate(data,headers=l,tablefmt='psql'),'\n')
        while True:
            ans=input('Do you want to delete any table?(its structure along '
                      +' with all data will be deleted..)(y/n)')
            if ans=='y':
                n=input('Enter table name:')
                a=input('Are you sure?(y/n)')
                if a=='y':
                    mycursor.execute('Drop table '+n)
                    mydb.commit()
                    print('Table',n,'deleted successfully...')
                else:
                    continue
            else:
                break

        print()        
        a=input('Do you want to revert back to main menu?(y/n):')
        if a=='y':
            base()
        else:
            print('Menu exited')
        
    elif k==2:
        while k==2:
               
            print('\n\n')
            while True:                                      #looped menu for book keeping system
                print('*'*10,'BOOK KEEPING MENU','*'*10)     #displaying menu items
                print('1.Adding Book records')
                print('2.Displaying details of all books')
                print('3.Searching')
                print('4.Deleting record of a particular book')
                print('5.Revert back to main menu')
                print('6.Exit')
                choice=input('Enter your choice:')
                #choice-output for book keeping menu starts
                if choice=='1':                                  #adding new record                             
                    while True:
                        i=int(input('Enter ISBN no.:'))
                        bn=input('Enter book name:')
                        a=input("Enter author's name:")
                        pn=input("Enter publisher's name:")
                        g=input('Enter genre:')
                        c=int(input('Enter no. of copies:'))
                        p=float(input('Enter price of single book:'))
                        query='insert into book_details'+' values({},"{}","{}","{}","{}",{},{})'.format(i,bn,a,g,pn,c,p)
                        #parameterised query for addition of new record    
                        mycursor.execute(query)
                        mydb.commit()
                        ans=input('Do you want to continue?(y/n):')
                        if ans=='n':
                            break           #terminates loop if user wants so
                    print('\n\n')
                if choice=='2':        #displaying complete data
                    print('Complete data of all the books:')
                    query='select * from book_details'
                    mycursor.execute(query)
                    data=mycursor.fetchall()
                    #displaying data in tabular form using tabulate fxn
                    print(tabulate(data,headers=["ISBN No.","Book Name","Author","Genre",
                                                 "Publisher\'s Name","No. of copies","Selling price"],tablefmt='psql'))
                    print('\n\n')
                if choice=='3':         #searching menu starts
                    while True:
                        print('*'*5,'SEARCHING MENU','*'*5)       #displaying elements of searching menu using simple print
                        print('1.Search by ISBN no. of book')
                        print('2.Search by Name')
                        print('3.Search by Author Name')
                        print('4.Search by Publisher\'s Name')
                        print('5.Search by Genre')
                        print('6.Revert back to previous menu')
                        c=int(input('Enter your choice:'))
                        if c==1:                           #search using ISBN no
                            while True:
                                i=int(input('Enter ISBN No. of the required book:'))
                                query='Select * from book_details where isbnno=%s'%(i,)
                                mycursor.execute(query)
                                data=mycursor.fetchall()
                                if data==[]:    #data will be none if no such row exists in main table
                                    print('Nothing to display')
                                else:
                                    print('Details:')
                                    print(tabulate(data,headers=["ISBN No.","Book Name","Author","Genre",
                                                                 "Publisher\'s Name","Genre","No. of copies","Selling price"],
                                                   tablefmt='psql'),'\n\n')
                                ans=input('Do you want to continue?(y/n):')            #to end search by isbn no. loop
                                if ans=='n':
                                    break
                                
                        if c==2:                 #search using title of book
                            while True:
                                n=input('Enter name of the book:')
                                query='Select * from book_details where bname="%s"'%(n,)
                                mycursor.execute(query)
                                data=mycursor.fetchall()
                                if data==[]:
                                    print('Nothing to display')
                                else:
                                    print('Details:')
                                    print(tabulate(data,headers=["ISBN No.","Book Name","Author",
                                                                 "Genre","Publisher\'s Name","No. of copies","Selling price"],
                                                   tablefmt='psql'),'\n\n')
                                ans=input('Do you want to continue?(y/n):')      #to end search by title name loop
                                if ans=='n':
                                    break
                        if c==3:            #search books using author name
                            while True:
                                a=input('Enter Author\'s name:')
                                query='Select * from book_details where author="%s"'%(a,)
                                mycursor.execute(query)
                                data=mycursor.fetchall()
                                if data==[]:
                                    print('Nothing to display')
                                else:
                                    print('Details:')
                                    print(tabulate(data,headers=["ISBN No.","Book Name","Author","Genre",
                                                                 "Publisher\'s Name","No. of copies","Selling price"],
                                                   tablefmt='psql'),'\n\n')
                                ans=input('Do you want to continue?(y/n):') #to end search by author name loop
                                if ans=='n':
                                    break
                        if c==4:        #to search books using publisher name
                            while True:
                                pn=input('Enter publisher\'s name:')
                                query='Select * from book_details where PName="%s"'%(pn,)
                                mycursor.execute(query)
                                data=mycursor.fetchall()
                                if data==[]:
                                    print('Nothing to display')
                                else:
                                    print('Details:')
                                    print(tabulate(data,headers=["ISBN No.","Book Name","Author","Genre",
                                                                 "Publisher\'s Name","No. of copies","Selling price"],
                                                   tablefmt='psql'),'\n\n')
                                ans=input('Do you want to continue?(y/n):')   #to end search by publisher name loop
                                if ans=='n':
                                    break      #to end search by publisher name
                        if c==5:     #to search books by genre
                            while True:
                                g=input('Enter genre:')
                                query='select * from book_details where genre="%s"'%(g,)
                                mycursor.execute(query)
                                data=mycursor.fetchall()
                                if data==[]:
                                    print('Nothing to Display')
                                else:
                                    print('details:')
                                    print(tabulate(data,headers=['ISBN No.','Book Name','Author',"Genre",
                                                                 "Publishe's name","No. of copies","Selling Price"],
                                                   tablefmt='psql'))
                                ans=input('Do you want to continue?(y/n):')  #to end search by genre loop
                                if ans=='n':
                                    break
                        if c==6:       
                            print('SEARCHING Menu exited')
                            break      # returns back to book keeping menu by ending the searching menu
                        
                            
                    
                            
                if choice=='4':           #deletion of a record from table book_details
                    while True:
                        i=int(input('Enter ISBN no. of the book whose record is to be deleted:'))
                        query='delete from book_details where isbnno=%s'%(i,)
                        mycursor.execute(query)
                        a=input('Are you sure you want to delete it?(y/n)')
                        if a=='y':
                            mydb.commit()
                            print('Details of book deleted successfully.')
                        ans=input('Do you want to continue?(y/n):')
                        if ans=='n':
                            break
                    print('\n\n')
                if choice=='6':    # exiting from the system
                    print('Menu exited')
                    k=4
                    break
                if choice=='5':     # back to main menu
                    print('Reverting back to main menu..')
                    base()      # calling the main menu fxn
                    k=4
                    break
          
    elif k==3:
        while k==3:
            
           
            while True:                                                #looped menu for issuing /returning system
                print('*'*10,'BOOK ISSUING/RETURNING MENU','*'*10)     #displaying menu items
                print('1.Issue')
                print('2.Return')
                print('3.Show past records of particular student') 
                print('4.Details of books yet to be returned')
                print('5.Revert back to main menu')
                print('6.Exit')
                choice=input('Enter your choice:')
                if choice=='1': # issuing book
                    while True:
                        i=input('Enter ISBN no. of the book:')       #taking req data from user
                        bn=input('Enter title of the book:')
                        sn=input('Enter name of student:')
                        a=int(input('Enter admission no.:'))
                        d=input('Enter issuing date(yyyy-mm-dd):')
                        query='insert into book_issue_return(Isbnno,bname,studname,admn,issuedate) values(%s,"%s","%s",%s,"%s")'%(i,bn,sn,a,d)
                        #query to insert record
                        mycursor.execute(query)
                        mydb.commit()
                        print('Book with title',bn,'issued to',sn,'on',d)
                        ans=input('Do you want to continue?(y/n)')   
                        if ans=='n':
                          break
                    print('\n\n')
                if choice=='2':   #returning book
                    while True:
                        i=int(input('Enter ISBN no. of the book:'))      #taking req data from user
                        mycursor.execute('select bname,returndate from book_issue_return where isbnno=%s'%(i,))
                        data=mycursor.fetchone()
                        if data==None:
                            print('No such book found in system')
                        elif data[1]==None:
                            print('Title of book to be returned:',data[0])
                            a=int(input('Enter admission no. of student:'))
                            d=input('Enter returning date(yyyy-mm-dd):')
                            query='UPDATE book_issue_return SET returndate="%s" WHERE isbnno=%s AND admn=%s'%(d,i,a)
                            #query to update record
                            mycursor.execute(query)
                            mydb.commit()
                            print('Data updated successfully..')
                        else:
                            print('Book already returned')
                        ans=input('Do you want to cotinue?(y/n):')
                        if ans=='n':
                            break
                    print('\n\n')
                if choice=='3':     #viewing details of particular student
                    while True:
                        n=input('Enter name of student:')
                        a=int(input('Enter Admission no.:'))
                        print('Details are..')
                        query='Select bname,isbnno,issuedate,ifnull(returndate,"Not yet")from book_issue_return where studname="%s" and admn=%s'%(n,a)
                        #query to show details
                        mycursor.execute(query)
                        data=mycursor.fetchall()
                        print(tabulate(data,headers=['Book Name','ISBN NO.',"Date Issued","Date Returned"],
                                       tablefmt='psql'))
                        #tabulating the fetched data
                        ans=input('Do you want to continue?(y/n)')
                        if ans=='n':
                            break
                    print('\n\n')
                if choice=='4':  #viewing details of books not returned yet
                    print('Details of student(s) yet to return book(s):')
                    query='select admn,studname,bname,isbnno,issuedate from book_issue_return where returndate IS NULL ORDER BY issuedate'
                    mycursor.execute(query)
                    data=mycursor.fetchall()
                    print(tabulate(data,headers=['Admission No.',"Student Name",
                                                 "Book name",'ISBN No.',"Date Issued"],tablefmt='psql'))
                    #tabulating the fetched data
                    print('\n\n')
                if choice=='5':  # back to main menu
                    print('Reverting back to main menu...')
                    base()
                    k=4
                    break
                if choice=='6': #exiting the system from current menu
                    print('Menu exited')
                    k=4
                    break
       
    elif k==4:
        print('Menu exited')
base()

                
            
        

    
        
            
            
            
        
    
    



