def calculate_perimeter(a, b, c):
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c
if __name__ == '__main__':
    sides1 = (3, 4, 5)
    try:
        perimeter1 = calculate_perimeter(*sides1)
        print(f"Perimeter of {sides1}: {perimeter1}")
    except ValueError as e:
        print(f"Error for {sides1}: {e}")
    sides2 = (1, 2, 5)
    try:
        perimeter2 = calculate_perimeter(*sides2)
        print(f"Perimeter of {sides2}: {perimeter2}")
    except ValueError as e:
        print(f"Error for {sides2}: {e}")
    sides3 = (5, 5, 10)
    try:
        perimeter3 = calculate_perimeter(*sides3)
        print(f"Perimeter of {sides3}: {perimeter3}")
    except ValueError as e:
        print(f"Error for {sides3}: {e}")
    sides4 = (2, 3, 1)
    try:
        perimeter4 = calculate_perimeter(*sides4)
        print(f"Perimeter of {sides4}: {perimeter4}")
    except ValueError as e:
        print(f"Error for {sides4}: {e}")