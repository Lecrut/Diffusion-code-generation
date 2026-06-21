def get_middle_element(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    result = get_middle_element(sample_list)
    print(result)
    
    sample_list_even = [1, 3, 5, 7]
    result_even = get_middle_element(sample_list_even)
    print(result_even)