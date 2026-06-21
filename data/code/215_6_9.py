def find_largest_number(numbers):
    if not numbers:
        return None
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3.14, 2.71, 1.41, 9.81, 6.28]
    largest_number = find_largest_number(sample_numbers)
    print(largest_number)