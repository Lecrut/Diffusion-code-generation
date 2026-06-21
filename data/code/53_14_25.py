class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError('Side length cannot be negative')
        self.side_length = side_length

    @staticmethod
    def compute_perimeter(side_length):
        return 4 * side_length

if __name__ == '__main__':
    test_cases = [
        (0, 0),
        (1, 4),
        (2.5, 10),
        (10, 40)
    ]
    for i, (input_value, expected_output) in enumerate(test_cases):
        result = Square.compute_perimeter(input_value)
        assert result == expected_output, f'Test case {i + 1} failed: input({input_value}) => output({result}), expected({expected_output})'
    
    sample_square = Square(5)
    print(sample_square.compute_perimeter(sample_square.side_length))