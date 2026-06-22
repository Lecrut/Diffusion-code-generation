def rhombus_area(d1: int, d2: int) -> int:
    return (d1 * d2) // 4

def square_area(side: int) -> int:
    return side ** 2

def areas_equal(d1: int, d2: int, side: int) -> bool:
    return rhombus_area(d1, d2) == square_area(side)

if __name__ == '__main__':
    print(areas_equal(8, 6, 5))