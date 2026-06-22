import math

def average_of_integers(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        raise ValueError("Cannot compute average of an empty sequence")
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = average_of_integers(sample_data)
    print(result)