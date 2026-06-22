def sum_digits(number: int) -> int:
    absolute_value = abs(number)
    digit_string = str(absolute_value)
    digit_values = [int(char) for char in digit_string]
    total_sum = 0
    for value in digit_values:
        total_sum += value
    return total_sum

if __name__ == '__main__':
    sample_number = 98765432109876543210
    computed_result = sum_digits(sample_number)
    print(computed_result)