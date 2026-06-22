class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def area(self):
        return self.compute_area()

    def compute_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_squares = [
        {'size': 'tiny', 'length': 1},
        {'size': 'medium', 'length': 6},
        {'size': 'huge', 'length': 12}
    ]
    
    for square_info in sample_squares:
        size_label = square_info['size']
        side_length = square_info['length']
        try:
            square_instance = Square(side_length)
            area_result = square_instance.area()
            print(f"The area of a {size_label} square with side length {side_length} is: {area_result}")
        except ValueError as e:
            print(e)