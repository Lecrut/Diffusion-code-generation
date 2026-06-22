numbers = [1, 2, 3, 4, 5]

def print_numbers_ten_times(numbers):
    for number in numbers:
        for _ in range(10):
            print(number)

if __name__ == '__main__':
    print_numbers_ten_times(numbers)