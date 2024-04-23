class Library:
    def __init__(self, booklist,name):
        print("Welcome to Smartstudy  ")
        self.book_list = booklist
        self.name = name
        self.lendedlist = {}
    
    def displaybooks(self):
        
        print(f"We have following books in : {self.name}")
        for book in self.book_list:
            print(book)

        
    def lend(self,user,book):
        if book not in self.lendedlist:
            self.lendedlist.update({book:user})
            print("book database has been updated, you may take the book now")
        else:
            print(f"book already issued by {self.lendedlist[book]}")
       
        
    def addbook(self,book):
        self.book_list.append(book)
        print("new book added")

    def returnbook(self,book):
        self.lendedlist.pop(book)

o1 = Library(["C++","C#","PYTHON","R","JAVA"], "Darshit's library")
# o1.displaybooks()
i=0
while i<100:

    print(f"welcome to {o1.name} \n Enter your choice")
    i+=1
    X = int(input("Press 1 to display Available Books \n Press 2 to borrow a Book \n Press 3 to return a Book \n Press 4 to add newbook \n Press 0 to quit"))
    if X == 0:
        break
    if X==1:
        o1.displaybooks()
          
    elif X==2:
        book = input("enter book name you ant to borrow")
        name = input("enter your name")
        o1.lend(name,book)

    elif X==4:
        book = input("enter book you want to add")
        o1.addbook(book)

    elif X==3:
        book =  input("enter book u wish to return")
        o1.returnbook(book)
        print("THANKYOU")

    else:
        print("inavlid choice")
        continue

          



        
