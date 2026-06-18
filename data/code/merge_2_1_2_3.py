def is_strictly_increasing(numbers):
    if len(numbers) <= 1:
        return True
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False
    return True
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = is_strictly_increasing(sample_list)
    print(result)