class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

def validate_input(value):
    try:
        float_value = float(value)
        if float_value <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return float_value
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    sample_length = "7"
    sample_width = "3"
    
    try:
        length = validate_input(sample_length)
        width = validate_input(sample_width)
        rectangle = Rectangle(length, width)
        perimeter = rectangle.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)