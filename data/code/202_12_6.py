def find_largest_number(numbers):
    return max(map(float, numbers))

if __name__ == '__main__':
    sample_numbers = [3, 5.2, '4', 2.8, '6.1']
    largest_number = find_largest_number(sample_numbers)
    print(largest_number)