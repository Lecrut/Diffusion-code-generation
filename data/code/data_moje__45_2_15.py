def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [3.5, 1.2, 4.8, 0.9, 2.1]
    result = find_minimum(sample_list)
    print(result)