def calculate_average(numbers):
    if not numbers:
        raise ValueError("Sample cannot be empty")
    
    total = sum(x for x in numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample = [50, 60, 70]
    avg = calculate_average(sample)
    print(avg)