from googlesearch import search

data = input("Enter Your Search: ")

for i in search(data, 10, advanced=True):
    print(i.url)
    print(i.title)
    print(i.description)
    print()
    print()