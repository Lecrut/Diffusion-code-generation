def validate_array(arr):
    if not arr:
        raise ValueError("Array must not be empty")
    for item in arr:
        if not isinstance(item, (int, float)):
            raise ValueError("All elements of the array must be numbers")

def calculate_mean(arr):
    validate_array(arr)
    total = sum(arr)
    count = len(arr)
    average = total / count
    return average

if __name__ == '__main__':
    sample_array = [4, 8, 12, 16]
    result = calculate_mean(sample_array)
    print(result)