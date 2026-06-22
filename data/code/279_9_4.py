def print_divisible_by_3_and_5(start, end):
    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            print(number)

if __name__ == '__main__':
    start_value = 1
    end_value = 100
    print_divisible_by_3_and_5(start_value, end_value)