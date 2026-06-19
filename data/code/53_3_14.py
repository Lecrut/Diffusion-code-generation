import argparse

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        if self.side_length > 0:
            return self.side_length * self.side_length
        else:
            raise ValueError("Invalid input: Side length must be positive")

def main():
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    args = parser.parse_args()
    
    try:
        square = Square(args.side_length)
        print(square.calculate_area())
        
        sample_square = Square(5.0)
        print(sample_square.calculate_area())
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()