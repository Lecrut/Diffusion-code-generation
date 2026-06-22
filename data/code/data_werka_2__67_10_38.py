def validate_input(arr, target):
    if not isinstance(arr, list) or not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Array must be a list of numbers")
    if not isinstance(target, (int, float)):
        raise ValueError("Target must be a number")

def find_two_sum(arr, target):
    validate_input(arr, target)
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    raise ValueError("No two elements sum up to the target value")

if __name__ == '__main__':
    sample_array = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
    target_value = 8.0
    result = find_two_sum(sample_array, target_value)
    print(result)