def find_smallest_element(numbers):
    return sorted(numbers)[0]

if __name__ == '__main__':
    sample_numbers = [34, 12, 98, 56, 23]
    print(find_smallest_element(sample_numbers))