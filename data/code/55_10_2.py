import sys
def calculate_perimeter(side_a, side_b, side_c):
    return side_a + side_b + side_c
if __name__ == '__main__':
    side_a = 5
    side_b = 12
    side_c = 13
    perimeter = calculate_perimeter(side_a, side_b, side_c)
    print(f"Side A: {side_a}")
    print(f"Side B: {side_b}")
    print(f"Side C: {side_c}")
    print(f"Perimeter: {perimeter}")