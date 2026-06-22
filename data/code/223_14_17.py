def find_maximum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    result = find_maximum(sample_data)
    print(result)