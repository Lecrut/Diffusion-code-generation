numbers = {i: i for i in range(10)}

def print_numbers(numbers_dict):
    for number in numbers_dict.values():
        print(number)

if __name__ == '__main__':
    print_numbers(numbers)