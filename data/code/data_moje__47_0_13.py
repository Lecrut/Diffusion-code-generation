def calculate_arithmetic_mean(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    mean = calculate_arithmetic_mean(sample_values)
    print(mean)
    
    sample_values_2 = [10.5, 20.3, 30.2]
    mean_2 = calculate_arithmetic_mean(sample_values_2)
    print(mean_2)
    
    try:
        calculate_arithmetic_mean([])
    except ValueError as e:
        print("ValueError raised for empty list:", str(e))