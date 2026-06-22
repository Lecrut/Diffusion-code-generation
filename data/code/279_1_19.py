def print_uppercase_fruits(fruit_list):
    for fruit in fruit_list:
        if isinstance(fruit, str):
            print(fruit.upper())
        else:
            raise ValueError("All elements in the list must be strings")

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    try:
        print_uppercase_fruits(fruits)
    except ValueError as e:
        print(e)