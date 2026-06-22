import itertools

def calculate_running_total(numbers):
    return tuple(itertools.accumulate(numbers))

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50)
    print(calculate_running_total(sample_values))