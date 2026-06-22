def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

if __name__ == '__main__':
    sample_list = [4, 2, 9, 1, 5]
    try:
        min_value = find_minimum(sample_list)
        print(f"Minimum of {sample_list}: {min_value}")
    except ValueError as e:
        print(e)