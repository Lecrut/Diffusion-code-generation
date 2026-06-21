def get_largest(data_set):
    if not data_set:
        raise ValueError("Input set cannot be empty")
    return max(data_set)

if __name__ == '__main__':
    sample_set = {4, 8, 15, 16, 23, 42}
    print(f"Largest in {sample_set}: {get_largest(sample_set)}")