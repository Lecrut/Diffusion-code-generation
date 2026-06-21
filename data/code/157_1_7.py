def find_smallest_element(numbers):
    return sorted(numbers)[0]

if __name__ == '__main__':
    sample_numbers = [5, 3, 9, 1, 4]
    smallest_number = find_smallest_element(sample_numbers)
    print(smallest_number)