def find_largest_element(*args):
    return max(args)

if __name__ == '__main__':
    numbers = (34, 78, 29, 56, 12)
    largest_number = find_largest_element(*numbers)
    print(largest_number)