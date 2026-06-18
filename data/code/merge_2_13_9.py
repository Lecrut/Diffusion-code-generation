import operator
from functools import reduce
def find_peak(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    return max(numbers)
if __name__ == '__main__':
    sample_data = [3, 7, 2, 9, 15, -4, 0]
    peak_value = find_peak(sample_data)
    print(peak_value)