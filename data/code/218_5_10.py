import sys

MIN_VALUE = float('inf')

def find_minimum(data):
    minimum = MIN_VALUE
    for number in data:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_data = [15, 3, 8, 22, 1]
    result = find_minimum(sample_data)
    print(result)