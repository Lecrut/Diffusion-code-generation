def find_minimum(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    sample_list = [4, 2, 9, 1, 5]
    result = find_minimum(sample_list)
    print(result)