def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_numbers = [5, 3, 9, 1, 4]
    print(find_smallest(sample_numbers))