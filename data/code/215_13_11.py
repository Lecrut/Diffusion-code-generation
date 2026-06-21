def find_largest_number(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 1.9, 5.6]
    print(find_largest_number(sample_numbers))