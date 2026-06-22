class RhombusGeometry:
    DIAGONAL_MULTIPLIER = 0.5

    def __init__(self, diagonal_1: float, diagonal_2: float):
        self.d1 = diagonal_1
        self.d2 = diagonal_2

    def compute_area(self) -> float:
        return self.d1 * self.d2 * self.DIAGONAL_MULTIPLIER

if __name__ == '__main__':
    shape_config = {
        'name': 'RhombusA',
        'd1': 12,
        'd2': 15
    }
    
    rhombus = RhombusGeometry(
        diagonal_1=shape_config['d1'],
        diagonal_2=shape_config['d2']
    )
    
    area_value = rhombus.compute_area()
    print(area_value)