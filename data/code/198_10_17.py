def find_minimum(numbers):
    if not numbers:
        return None
    minimum = min(numbers)
    return minimum
if __name__ == '__main__':
    sample_data = [42, 15, 89, 3, 76, 22]
    result = find_minimum(sample_data)
    print(result)