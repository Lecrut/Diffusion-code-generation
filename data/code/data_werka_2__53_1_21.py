class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    side_lengths = {
        'small': 3,
        'medium': 6,
        'large': 9
    }
    
    sample_size = 'medium'
    square_instance = Square(side_lengths[sample_size])
    computed_area = square_instance.calculate_area()
    print(f"The area of a {sample_size} square is: {computed_area}")