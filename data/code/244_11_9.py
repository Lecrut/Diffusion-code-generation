def compute_square_area(side_length):
    return side_length ** 2

def sum_of_areas(side1, side2):
    area1 = compute_square_area(side1)
    area2 = compute_square_area(side2)
    return area1 + area2

if __name__ == '__main__':
    a = 5
    b = 3
    result = sum_of_areas(a, b)
    print(result)