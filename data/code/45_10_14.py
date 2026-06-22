def find_minimum(numbers):
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [10, 5, 23, 2, 8, 99, 34]
    print(find_minimum(sample_list))