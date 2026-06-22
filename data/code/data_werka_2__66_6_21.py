def compare_adjacent_numbers(elements):
    for i in range(len(elements) - 1):
        if not (isinstance(elements[i], (int, float)) and isinstance(elements[i + 1], (int, float))):
            raise TypeError(f"Non-numeric adjacent elements found: {elements[i]} and {elements[i + 1]}")
        if elements[i] > elements[i + 1]:
            return True
    return False

if __name__ == '__main__':
    sample_values = [3, 5, 'a', 7.2, 8]
    try:
        result = compare_adjacent_numbers(sample_values)
        print(result)
    except TypeError as e:
        print(e)