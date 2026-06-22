def calculate_average(numbers):
    if not isinstance(numbers, tuple) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input must be a tuple of integers.")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values1 = (10, 20, 30, 40, 50)
    average1 = calculate_average(sample_values1)
    print(f"The average of {sample_values1} is: {average1}")

    sample_values2 = (5, 15, 25, 35)
    average2 = calculate_average(sample_values2)
    print(f"The average of {sample_values2} is: {average2}")

    sample_values3 = ()
    try:
        average3 = calculate_average(sample_values3)
        print(f"The average of {sample_values3} is: {average3}")
    except ValueError as e:
        print(e)

    sample_values4 = (1, 2, 3, 4.5)
    try:
        average4 = calculate_average(sample_values4)
        print(f"The average of {sample_values4} is: {average4}")
    except ValueError as e:
        print(e)