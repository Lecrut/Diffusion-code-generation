def get_middle_element(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

if __name__ == '__main__':
    sample_data = {
        "odd_count": [1, 3, 5, 7, 9],
        "even_count": [1, 3, 5, 7],
        "single": [42]
    }
    for key, val in sample_data.items():
        result = get_middle_element(val)
        print(result)