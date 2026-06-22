def max_element(iterable):
    if not iterable:
        raise ValueError("Empty iterable")
    return max(iterable)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(max_element(sample_values))