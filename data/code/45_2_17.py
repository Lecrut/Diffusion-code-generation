def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.1, 3.3]
    result = find_minimum(sample_values)
    print(result)