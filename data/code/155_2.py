def calculate_float_sum(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total
if __name__ == '__main__':
    sample_list = [1.5, 2.75, 3.0, -4.2, 0.1]
    result = calculate_float_sum(sample_list)
    print(result)