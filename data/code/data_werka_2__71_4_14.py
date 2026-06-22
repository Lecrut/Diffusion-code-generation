def get_middle_element(numbers):
    if not numbers:
        raise ValueError("Input list is empty.")
    left = 0
    right = len(numbers) - 1
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] < numbers[mid + 1]:
            left = mid
        else:
            right = mid
    if left == right:
        return numbers[left]
    return (numbers[left] + numbers[right]) / 2

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45, 55]
    try:
        result = get_middle_element(sample_numbers)
        print(result)
    except ValueError as e:
        print(e)