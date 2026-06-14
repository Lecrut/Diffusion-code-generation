def find_maximum(numbers):
    if not numbers:
        return None
    current_max = numbers[0]
    for number in numbers[1:]:
        if number > current_max:
            current_max = number
    return current_max
if __name__ == '__main__':
    sample_numbers = [15, 7, 22, 3, 45, 10]
    maximum_value = find_maximum(sample_numbers)
    print(maximum_value)