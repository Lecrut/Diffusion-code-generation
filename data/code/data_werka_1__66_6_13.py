def compare_adjacent_numbers(elements):
    for i in range(len(elements) - 1):
        if isinstance(elements[i], (int, float)) and isinstance(elements[i + 1], (int, float)):
            continue
        else:
            raise TypeError(f"Non-numeric adjacent elements found: {elements[i]} and {elements[i + 1]}")

if __name__ == '__main__':
    sample_values = [10, 20.5, 'hello', 30, 40.1, 'world']
    try:
        compare_adjacent_numbers(sample_values)
    except TypeError as e:
        print(e)