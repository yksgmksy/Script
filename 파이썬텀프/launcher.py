loopFlag = 1
from internetcountry import *

#### Menu  implementation
def printMenu():
    print("\nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Book list: b")
    #print("Add new book: a")
    print("SearchCountry Title: e")
    print("SortByGround: s")
    #print("Make html: m")
    print("----------------------------------------")
    print("Get book data from isbn: g")
    print("send maIl : i")
    print("sTart Web Service: t")
    print("========Menu==========")
    
def launcherFunction(menu):
    if menu ==  'l':
        LoadXMLFromFile()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'p':
        PrintDOMtoXML()
    elif menu == 'b':
        PrintCountryList(["countryName",])
    elif menu == 'e':
        keyword = str(input ('input keyword to search :'))
        printBookList(SearchCountryName(keyword))
    elif menu == 'g': 
        isbn = str(input ('input isbn to get :'))
        #isbn = '0596513984'
        ret = getBookDataFromISBN(isbn)
        AddBook(ret)
    elif menu == 'm':
        keyword = str(input ('input keyword code to the html  :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print("-----------------------")
        print(html)
        print("-----------------------")
    elif menu == 's':
        #countrylist,groundlist = SortToGround()
        SortToGround()
        
    elif menu == 'i':
        sendMain()
    elif menu == "t":
        startWebService()
    else:
        print ("error : unknow menu key")

def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()
    
##### run #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")
