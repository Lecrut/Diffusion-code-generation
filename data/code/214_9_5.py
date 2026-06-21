def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 10]
    print(find_smallest(sample_values))