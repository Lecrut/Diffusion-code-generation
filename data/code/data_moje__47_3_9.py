def average(numbers):
    if not numbers:
        raise ValueError("Cannot compute average of an empty sequence")
    return sum(numbers) / len(numbers)

def average_generator(numbers):
    if not numbers:
        raise ValueError("Cannot compute average of an empty sequence")
    total = sum(x for x in numbers)
    count = sum(1 for _ in numbers)
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = average_generator(sample_values)
    print(result)