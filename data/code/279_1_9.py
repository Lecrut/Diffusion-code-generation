fruits = {'apple': 'APPLE', 'banana': 'BANANA', 'cherry': 'CHERRY'}

def print_fruits_uppercase(fruit_list):
    for fruit in fruit_list:
        print(fruits[fruit])

if __name__ == '__main__':
    fruits_to_print = ['apple', 'banana', 'cherry']
    print_fruits_uppercase(fruits_to_print)