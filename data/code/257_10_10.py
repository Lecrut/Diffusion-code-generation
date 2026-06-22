def calculate_difference(numbers: list) -> int:
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    nums = [12, 45, 7, 89, 3]
    result = calculate_difference(nums)
    print(result)