def find_largest_number(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_data = [10, 5, 20, 8, 15]
    print(find_largest_number(sample_data))