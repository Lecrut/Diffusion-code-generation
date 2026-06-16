def is_strictly_increasing(numbers):
    if len(numbers) <= 1:
        return True
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            return False
    return True
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = is_strictly_increasing(sample_data)
    print(result)