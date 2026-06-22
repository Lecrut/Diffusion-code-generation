def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return min(numbers)

if __name__ == '__main__':
    sample_list = [34, 12, 56, 4, 98, 23, 5]
    result = find_minimum(sample_list)
    print(result)