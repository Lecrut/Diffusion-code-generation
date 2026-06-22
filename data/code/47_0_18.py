def calculate_arithmetic_mean(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.0, 4.5]
    result = calculate_arithmetic_mean(sample_values)
    print(result)
    empty_list = []
    try:
        calculate_arithmetic_mean(empty_list)
    except ValueError as e:
        print(e)