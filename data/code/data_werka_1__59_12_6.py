def find_middle_item(numbers):
    n = len(numbers)
    if n == 0:
        return None
    index = n // 2
    if n % 2 == 1:
        return numbers[index]
    else:
        return (numbers[index - 1] + numbers[index]) // 2

if __name__ == '__main__':
    sample_values = [3, 7, 2, 9, 4]
    result = find_middle_item(sample_values)
    print(result)