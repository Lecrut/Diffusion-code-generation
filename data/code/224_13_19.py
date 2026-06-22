def calculate_mean(arr):
    if not arr:
        raise ValueError("Array must not be empty")
    return sum(arr) / len(arr)

if __name__ == '__main__':
    sample_array = [4, 8, 12, 16]
    try:
        print(calculate_mean(sample_array))
    except ValueError as e:
        print(e)