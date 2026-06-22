def calculate_mean(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    return sum(arr) / len(arr)

if __name__ == '__main__':
    sample_array = [4, 8, 12, 16]
    print(calculate_mean(sample_array))