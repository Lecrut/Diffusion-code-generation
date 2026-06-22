def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return min(filter(lambda x: isinstance(x, (int, float)), numbers))

if __name__ == '__main__':
    sample_list = [10, 3.14, 5, -2.5, 100, "a", 0]
    result = find_minimum(sample_list)
    print(result)