def sum_numbers(data):
    if not all(isinstance(num, (int, float)) for num in data):
        raise ValueError("All elements in the sequence must be numbers")
    return sum(data)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = sum_numbers(sample_values)
    print(result)