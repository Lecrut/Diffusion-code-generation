def find_minimum(numbers):
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 67, 19, 23]
    result = find_minimum(sample_list)
    print(result)