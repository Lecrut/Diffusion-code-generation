def calculate_triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sum of any two sides must be greater than the third side.")
    
    semi_perimeter = (a + b + c) / 2
    area = (semi_perimeter * 
            (semi_perimeter - a) * 
            (semi_perimeter - b) * 
            (semi_perimeter - c)) ** 0.5
    
    return area

if __name__ == '__main__':
    try:
        side1 = 7
        side2 = 8
        side3 = 9
        print(calculate_triangle_area(side1, side2, side3))
    except ValueError as e:
        print(e)