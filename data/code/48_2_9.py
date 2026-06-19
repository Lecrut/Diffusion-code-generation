def can_form_triangle(sides):
    if len(sides) != 3:
        return False
    side1, side2, side3 = sides
    is_valid = (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)
    return is_valid

if __name__ == '__main__':
    sample_values = [7, 10, 5]
    print(can_form_triangle(sample_values))