MAX_VALUE = float('inf')
MIN_VALUE = float('-inf')

def calculate_difference(numbers: list) -> int:
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 9, 1, 7, 5]
    result = calculate_difference(sample_values)
    print(result)