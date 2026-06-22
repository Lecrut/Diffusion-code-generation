def is_even(number):
    return number % 2 == 0

def cycle_and_print_evens(start, end):
    for num in range(start, end + 1):
        if is_even(num):
            print(num)

if __name__ == '__main__':
    start_val = 100
    end_val = 200
    cycle_and_print_evens(start_val, end_val)