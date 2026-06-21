def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

if __name__ == '__main__':
    try:
        sample_values = [10, 20, 30, 40, 50]
        print(calculate_average(sample_values))
    except ValueError as e:
        print(e)