def calculate_mean(arr):
    if not arr or not isinstance(arr, list) or not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Input must be a non-empty list of numbers")
    return sum(arr) / len(arr)

if __name__ == '__main__':
    sample_array = [4, 8, 12, 16]
    try:
        result = calculate_mean(sample_array)
        print(result)
    except ValueError as e:
        print(e)