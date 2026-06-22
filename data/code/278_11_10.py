def print_items_separately(items):
    for item in items:
        print(item)

if __name__ == '__main__':
    data1 = ('apple', 'banana', 'cherry')
    data2 = ()
    
    print("Printing tuple items separately:")
    print_items_separately(data1)
    
    if data2:
        print("\nPrinting tuple items separately:")
        print_items_separately(data2)
    else:
        print("\nEmpty tuple, nothing to print.")