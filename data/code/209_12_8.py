def average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        raise ValueError("Input is not iterable")
    except ZeroDivisionError:
        raise ValueError("Empty sequence")

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(average(sample_values))