def get_largest(data_set):
    if not data_set:
        raise ValueError("Input set cannot be empty")
    return max(data_set)

if __name__ == '__main__':
    sample_set = {4, 8, 15, 16, 23, 42}
    try:
        print(f"Largest in the set: {get_largest(sample_set)}")
    except ValueError as e:
        print(e)