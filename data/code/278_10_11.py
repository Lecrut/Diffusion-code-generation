ITEMS_TO_PRINT = [
    "Apple",
    "Banana",
    "Cherry",
    123,
    "Date"
]

def print_items(item_list):
    for item in item_list:
        print(item)

if __name__ == '__main__':
    print_items(ITEMS_TO_PRINT)