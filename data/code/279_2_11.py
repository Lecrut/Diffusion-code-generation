def print_even_numbers(start=100, end=200):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

if __name__ == '__main__':
    start_val = 130
    end_val = 150
    print_even_numbers(start_val, end_val)