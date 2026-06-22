def find_max(iterable):
    max_value = iterable[0]
    for value in iterable:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_max(sample_values))