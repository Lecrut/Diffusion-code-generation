def find_maximum(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum
if __name__ == '__main__':
    sample_list = [3, 7, 2, 9, 4, 8]
    result = find_maximum(sample_list)
    print(result)