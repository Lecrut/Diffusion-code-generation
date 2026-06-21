def find_lowest_value(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    lowest = float('inf')
    for number in numbers:
        if number < lowest:
            lowest = number
    
    return lowest

if __name__ == '__main__':
    test_cases = [
        [-5, 2],
        [10, -8],
        [],
        [3, 7],
        [-1, 9],
        [100]
    ]
    
    for case in test_cases:
        try:
            print(f"Lowest value in {case}: {find_lowest_value(case)}")
        except ValueError as e:
            print(e)