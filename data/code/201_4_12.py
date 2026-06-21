def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    total = sum(number for number in numbers)
    count = len(numbers)
    
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    average_result = calculate_average(sample_values)
    print(f"Average of {sample_values}: {average_result}")