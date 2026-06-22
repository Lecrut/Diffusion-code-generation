def min_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    return min([x for x in numbers])

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = min_value(sample_list)
    print(result)