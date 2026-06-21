def calculate_positive_sum(numbers):
    positive_sum = 0
    for number in numbers:
        if number > 0:
            positive_sum += number
    return positive_sum

if __name__ == '__main__':
    sample_numbers = [2.5, -1.2, 3.7, 4.1, 0.0, -2.8]
    result = calculate_positive_sum(sample_numbers)
    print(result)