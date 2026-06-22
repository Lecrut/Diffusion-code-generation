def print_positive_numbers(start, end):
    for num in range(start, end + 1):
        if num > 0:
            print(num)

if __name__ == '__main__':
    start = -5
    end = 5
    print_positive_numbers(start, end)