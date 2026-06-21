def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    return average

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    try:
        avg = calculate_average(sample_numbers)
        print(f"The calculated average is: {avg}")
    except ValueError as e:
        print(e)