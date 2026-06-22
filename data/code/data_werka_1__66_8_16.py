def compare_adjacent(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if len(numbers) < 2:
        return []
    
    result = []
    for i in range(len(numbers) - 1):
        result.append(numbers[i] <= numbers[i + 1])
    
    return result

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2]
    try:
        result = compare_adjacent(sample_array)
        print(result)
    except Exception as e:
        print(e)