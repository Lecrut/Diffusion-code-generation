def print_items(item_list):
    for item in item_list:
        print(item)

if __name__ == '__main__':
    fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
    fruit_names = list(fruits.keys())
    print_items(fruit_names)