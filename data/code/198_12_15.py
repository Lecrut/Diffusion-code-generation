MIN_VALUE = float('inf')

def find_smallest_value(numbers):
    smallest = MIN_VALUE
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [-5, 2, -8, 10]
    print(find_smallest_value(sample_values))