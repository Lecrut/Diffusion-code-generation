import math

def average_integers(numbers):
    if not numbers:
        return 0
    return sum(n for n in numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = average_integers(sample_data)
    print(result)