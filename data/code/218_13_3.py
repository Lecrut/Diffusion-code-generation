def find_smallest(numbers):
    return min(numbers)

if __name__ == '__main__':
    numbers = [10, 23, -5, 78, 0]
    smallest_number = find_smallest(numbers)
    print(smallest_number)