def print_items(item_list):
    for item in item_list:
        print(item)

if __name__ == '__main__':
    fruits = ["Apple", "Banana", "Cherry"]
    numbers = [1, 2, 3]
    mixed = [True, False, None]

    combined_list = fruits + numbers + mixed
    print_items(combined_list)