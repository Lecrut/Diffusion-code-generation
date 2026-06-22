def is_even(number):
    return number % 2 == 0

def print_even_numbers_in_range(start, end):
    for num in range(start, end + 1):
        if is_even(num):
            print(num)

if __name__ == '__main__':
    start_val = 100
    end_val = 200
    print_even_numbers_in_range(start_val, end_val)