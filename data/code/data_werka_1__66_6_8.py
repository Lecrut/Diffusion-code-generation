def compare_adjacent_numbers(elements):
    for i in range(len(elements) - 1):
        if isinstance(elements[i], (int, float)) and isinstance(elements[i + 1], (int, float)):
            continue
        elif not isinstance(elements[i], (int, float)) or not isinstance(elements[i + 1], (int, float)):
            raise TypeError(f"Non-numeric adjacent elements found: {elements[i]} and {elements[i + 1]}")

if __name__ == '__main__':
    sample_values = [1, 2.5, 'a', 4, 5, 'b']
    try:
        compare_adjacent_numbers(sample_values)
    except TypeError as e:
        print(e)