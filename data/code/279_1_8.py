def print_fruits(fruit_list):
    if not isinstance(fruit_list, list) or not all(isinstance(fruit, str) for fruit in fruit_list):
        raise ValueError("Input must be a list of strings")
    for fruit in fruit_list:
        print(fruit.upper())

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry']
    print_fruits(fruits)