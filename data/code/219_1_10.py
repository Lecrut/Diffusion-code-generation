def max_element(iterable):
    try:
        return max(iterable)
    except ValueError as e:
        raise ValueError("Empty iterable") from e

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(max_element(sample_values))