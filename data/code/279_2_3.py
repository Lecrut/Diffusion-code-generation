def cycle_and_print_evens(start, end):
    evens = [num for num in range(start, end + 1) if num % 2 == 0]
    return evens

if __name__ == '__main__':
    start_val = 150
    end_val = 170
    even_numbers = cycle_and_print_evens(start_val, end_val)
    print(even_numbers)