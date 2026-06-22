def print_positive_numbers(start, end):
    for num in range(start, end + 1):
        if num > 0:
            print(num)

if __name__ == '__main__':
    start_value = -5
    end_value = 5
    print_positive_numbers(start_value, end_value)