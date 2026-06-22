EVEN_THRESHOLD = 2

def is_even(number):
    return number % EVEN_THRESHOLD == 0

def print_even_numbers(start, end):
    for num in range(start, end + 1):
        if is_even(num):
            print(num)

if __name__ == '__main__':
    start_val = 100
    end_val = 200
    print_even_numbers(start_val, end_val)