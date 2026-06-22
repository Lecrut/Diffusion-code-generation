def find_difference(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError('Both inputs must be numbers')
    return abs(num1 - num2)
if __name__ == '__main__':
    try:
        sample_pairs = [(10, 4), (-5, 15), (7.5, 3.2), (0, 0), ('a', 5)]
        for pair in sample_pairs:
            result = find_difference(*pair)
            print(f'The absolute difference between {pair[0]} and {pair[1]} is: {result}')
    except ValueError as e:
        print(e)