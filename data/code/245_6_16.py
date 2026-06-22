class AreaComparison:
    @staticmethod
    def calculate_rhombus_area(diag1: int, diag2: int) -> int:
        return (diag1 * diag2) // 4
    
    @staticmethod
    def calculate_square_area(side_length: int) -> int:
        return side_length ** 2
    
    @classmethod
    def areas_equal(cls, diag1: int, diag2: int, side_length: int) -> bool:
        area_rhombus = cls.calculate_rhombus_area(diag1, diag2)
        area_square = cls.calculate_square_area(side_length)
        return area_rhombus == area_square

if __name__ == '__main__':
    print(AreaComparison.areas_equal(8, 6, 5))