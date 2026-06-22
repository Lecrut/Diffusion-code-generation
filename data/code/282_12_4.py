def calculate_total(numbers):
    return sum(x for x in numbers)

if __name__ == '__main__':
    sample_numbers = [2.5, 3.4, 1.8, 0.9]
    result = calculate_total(sample_numbers)
    print(f"The total for {sample_numbers} is: {result}")