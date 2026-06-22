def get_middle_element(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_list)
    print(result)