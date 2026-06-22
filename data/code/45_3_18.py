def get_minimum(numbers):
    if not numbers:
        return None
    return min(numbers)

if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 7]
    result = get_minimum(sample_data)
    print(result)