import math
def analyze_numbers(numbers):
    if not numbers:
        return None, None, None
    minimum = numbers[0]
    maximum = numbers[0]
    total_sum = 0
    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
        total_sum += number
    return minimum, maximum, total_sum
if __name__ == '__main__':
    sample_numbers = [15, 8, 22, 4, 30, 11]
    minimum_val, maximum_val, total_sum = analyze_numbers(sample_numbers)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")
    print(f"Sum: {total_sum}")