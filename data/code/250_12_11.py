def calculate_average(numbers):
    if not numbers:
        return 0
    
    total = sum(numbers)
    count = len(numbers)
    
    if count == 0:
        raise ValueError("No valid numbers were entered to calculate the average.")
    
    average = total / count
    return average

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45, 55]
    try:
        result = calculate_average(sample_numbers)
        print(f"The average of the entered numbers is: {result}")
    except ValueError as e:
        print(e)