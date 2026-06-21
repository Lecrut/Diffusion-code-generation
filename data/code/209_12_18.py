def average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        raise ValueError("Input must be an iterable of numbers")

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(average(sample_values))