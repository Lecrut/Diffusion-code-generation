def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9]
    try:
        result = find_minimum(sample_list)
        print(f"Minimum of {sample_list}: {result}")
    except ValueError as e:
        print(e)