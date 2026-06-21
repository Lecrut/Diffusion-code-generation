class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def area(self):
        return self.calculate_area()

    def calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_lengths = {
        'small': 3,
        'medium': 5,
        'large': 10
    }
    
    for size, length in sample_side_lengths.items():
        square = Square(length)
        print(f"The area of a {size} square with side length {length} is: {square.area()}")