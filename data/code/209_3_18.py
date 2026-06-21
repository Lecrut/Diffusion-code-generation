def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")
    
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_numbers = [5, 10, 15, 20, 25]
    try:
        avg = calculate_average(sample_numbers)
        print(avg)
    except ValueError as e:
        print(e)