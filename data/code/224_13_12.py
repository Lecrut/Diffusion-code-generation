def calculate_mean(arr):
    if not arr:
        raise ValueError("Array must not be empty")
    total = sum(arr)
    count = len(arr)
    average = total / count
    return average

if __name__ == '__main__':
    sample_array = [4, 8, 12, 16]
    print(calculate_mean(sample_array))