def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must contain at least one element")
    return min(numbers)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_minimum(sample_list)
    print(result)