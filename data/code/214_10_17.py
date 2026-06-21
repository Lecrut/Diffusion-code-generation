INITIAL_VALUE = float('inf')

def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    min_value = INITIAL_VALUE
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_values = [10, 42, -3, 78, 0]
    print(find_minimum(sample_values))