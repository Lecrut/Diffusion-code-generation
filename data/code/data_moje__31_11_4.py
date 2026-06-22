SQUARE_CONSTANT = 2

def get_square_area(side):
    if side < 0:
        return -1
    return side * side

class SquareCalculator:
    def __init__(self, side_length):
        self.side_length = side_length
    
    def compute(self):
        return self.side_length ** SQUARE_CONSTANT

if __name__ == '__main__':
    fixed_input = 15
    area_result = get_square_area(fixed_input)
    print(area_result)
    calc_instance = SquareCalculator(fixed_input)
    print(calc_instance.compute())