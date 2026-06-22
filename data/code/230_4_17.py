import itertools

def calculate_running_total(numbers):
    try:
        return tuple(itertools.accumulate(numbers))
    except TypeError as e:
        raise ValueError("All elements in the input tuple must be numbers") from e

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    print(calculate_running_total(sample_numbers))