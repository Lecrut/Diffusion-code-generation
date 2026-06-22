def check_triangle_validity(side_one, side_two, side_three):
    sides = [side_one, side_two, side_three]
    all_positive = all(s > 0 for s in sides)
    if not all_positive:
        return False
    sorted_sides = sorted(sides)
    smallest = sorted_sides[0]
    middle = sorted_sides[1]
    largest = sorted_sides[2]
    triangle_inequality_holds = (smallest + middle) > largest
    return triangle_inequality_holds

if __name__ == '__main__':
    val1 = check_triangle_validity(5, 12, 13)
    val2 = check_triangle_validity(1, 1, 10)
    val3 = check_triangle_validity(-3, 4, 5)
    val4 = check_triangle_validity(0, 0, 0)
    val5 = check_triangle_validity(7, 7, 7)
    print(val1)
    print(val2)
    print(val3)
    print(val4)
    print(val5)