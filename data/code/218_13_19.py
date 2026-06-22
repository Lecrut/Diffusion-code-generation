def find_smallest_number(numbers):
    return min(numbers)

if __name__ == '__main__':
    numbers = [42, 3.14, -5, 0, 23]
    smallest_number = find_smallest_number(numbers)
    print(smallest_number)