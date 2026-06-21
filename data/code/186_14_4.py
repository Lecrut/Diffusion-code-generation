def sort_numerical_strings(numerical_strings):
    try:
        return sorted(map(int, numerical_strings))
    except ValueError as e:
        raise ValueError("All elements in the list must be valid integer strings") from e

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(sort_numerical_strings(sample_values))