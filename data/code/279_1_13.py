fruits = ['apple', 'banana', 'cherry']

def print_uppercase_fruits(fruit_list):
    for fruit in fruit_list:
        print(fruit.upper())

if __name__ == '__main__':
    sample_fruits = ['grape', 'orange', 'kiwi']
    print("Testing print_uppercase_fruits with sample fruits:")
    print_uppercase_fruits(sample_fruits)