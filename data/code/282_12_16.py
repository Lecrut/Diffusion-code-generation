CONVERSION_FACTOR = 1.0

def calculate_total(numbers):
    return sum(x * CONVERSION_FACTOR for x in numbers)

if __name__ == '__main__':
    sample_numbers_1 = [1.5, 2.3, 3.7, 4.1]
    result_1 = calculate_total(sample_numbers_1)
    print(f"The total for {sample_numbers_1} is: {result_1}")

    sample_numbers_2 = [-1.0, 5.5, -3.2, 10.1]
    result_2 = calculate_total(sample_numbers_2)
    print(f"The total for {sample_numbers_2} is: {result_2}")