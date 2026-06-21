def average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        raise ValueError("Input must be an iterable of numbers")

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(average(sample_numbers))