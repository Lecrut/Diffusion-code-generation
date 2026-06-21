def find_largest_number(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_data = [10, 5, 22, 8, 30]
    try:
        print(find_largest_number(sample_data))
    except ValueError as e:
        print(e)