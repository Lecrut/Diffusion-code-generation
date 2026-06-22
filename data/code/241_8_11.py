WIDTH = 5
HEIGHT = 10

def calculate_area(length: int, width: int) -> int:
    return length * width
if __name__ == '__main__':
    print(calculate_area(WIDTH, HEIGHT))
    print(calculate_area(3, 4))
    print(calculate_area(7, 2))
    print(calculate_area(10, 10))