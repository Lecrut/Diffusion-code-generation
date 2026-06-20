def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values1 = (2, 4, 6, 8)
    sample_values2 = (-5, -3, -1, 1, 3, 5)
    sample_values3 = ()
    
    avg1 = calculate_average(sample_values1)
    avg2 = calculate_average(sample_values2)
    avg3 = calculate_average(sample_values3)
    
    print(f"Average of {sample_values1}: {avg1}")
    print(f"Average of {sample_values2}: {avg2}")
    print(f"Average of {sample_values3}: {avg3}")