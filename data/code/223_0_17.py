def find_max_value(numbers):
    return max(numbers)

if __name__ == '__main__':
    sample_values = [
        [3, 1, 4, 1, 5, 9, 2],
        [-10, -5, -20, -1],
        [7],
        [42],
        []
    ]
    
    for values in sample_values:
        try:
            print(f"Maximum of {values}: {find_max_value(values)}")
        except ValueError as e:
            print(e)