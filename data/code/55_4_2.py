def calculate_perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c
if __name__ == '__main__':
    sides1 = (3, 4, 5)
    try:
        perimeter1 = calculate_perimeter(sides1[0], sides1[1], sides1[2])
        print(f"Perimeter of {sides1}: {perimeter1}")
    except ValueError as e:
        print(f"Error for {sides1}: {e}")
    sides2 = (1, 2, 5)
    try:
        perimeter2 = calculate_perimeter(sides2[0], sides2[1], sides2[2])
        print(f"Perimeter of {sides2}: {perimeter2}")
    except ValueError as e:
        print(f"Error for {sides2}: {e}")
    sides3 = (6, 8, 10)
    try:
        perimeter3 = calculate_perimeter(sides3[0], sides3[1], sides3[2])
        print(f"Perimeter of {sides3}: {perimeter3}")
    except ValueError as e:
        print(f"Error for {sides3}: {e}")
    sides4 = (2, 3, 1)
    try:
        perimeter4 = calculate_perimeter(sides4[0], sides4[1], sides4[2])
        print(f"Perimeter of {sides4}: {perimeter4}")
    except ValueError as e:
        print(f"Error for {sides4}: {e}")