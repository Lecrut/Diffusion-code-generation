def find_max(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 30, 1]
    print(find_max(sample_numbers))