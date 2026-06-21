def print_even_numbers(start, end, step):
    for num in range(start, end + 1, step):
        print(num)

if __name__ == '__main__':
    start_val = 2
    end_val = 20
    step_val = 2
    print_even_numbers(start_val, end_val, step_val)