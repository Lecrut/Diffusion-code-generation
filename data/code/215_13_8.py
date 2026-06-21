def find_largest_number(numbers):
    return max(numbers)

if __name__ == '__main__':
    NUMBERS = [3.5, 2.1, 4.8, 1.9, 5.6]
    largest_number = find_largest_number(NUMBERS)
    print(largest_number)