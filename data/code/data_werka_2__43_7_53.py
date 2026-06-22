class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def compute_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    square_configs = {
        'square1': {'side_length': 5},
        'square2': {'side_length': 8.2}
    }

    for config_name, config in square_configs.items():
        try:
            square = Square(config['side_length'])
            print(f"Area of {config_name} with side {config['side_length']}: {square.compute_area()}")
        except ValueError as e:
            print(e)