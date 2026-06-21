def sort_by_descending(numbers):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements in the list must be numbers.")
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [7.2, 3.1, 5.5, 2.4, 8.9]
    try:
        sorted_values = sort_by_descending(sample_values)
        print(sorted_values)
    except ValueError as e:
        print(e)