def find_largest(a, b, c):
    return max(a, b, c)

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 25,
        'c': 10
    }
    largest_value = find_largest(**sample_values)
    print(f"The largest value is: {largest_value}")