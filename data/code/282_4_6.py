def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = [1, 5, 10, 2]
    result = calculate_sum(sample_values)
    print(f"The sum of {sample_values} is: {result}")