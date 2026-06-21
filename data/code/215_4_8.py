def find_largest_value(data):
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    return max(data.values())

if __name__ == '__main__':
    sample_dict = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
    print(f"Largest value in {sample_dict}: {find_largest_value(sample_dict)}")