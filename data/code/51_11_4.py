def calculate_perimeter(sides):
    if not isinstance(sides, list):
        raise ValueError("Input must be a list of side lengths.")
    if not all(isinstance(side, (int, float)) for side in sides):
        raise ValueError("All elements in the list must be numeric.")
    return sum(sides)
if __name__ == '__main__':
    sample_sides_1 = [3, 4, 5]
    sample_sides_2 = [10.5, 2.5, 7.0]
    sample_sides_3 = [2, 'a', 5]
    sample_sides_4 = "not a list"
    sample_sides_5 = [1, 2, "three"]
    print(f"Perimeter of {sample_sides_1}: {calculate_perimeter(sample_sides_1)}")
    print(f"Perimeter of {sample_sides_2}: {calculate_perimeter(sample_sides_2)}")
    try:
        calculate_perimeter(sample_sides_3)
    except ValueError as e:
        print(f"Error for {sample_sides_3}: {e}")
    try:
        calculate_perimeter(sample_sides_4)
    except ValueError as e:
        print(f"Error for {sample_sides_4}: {e}")
    try:
        calculate_perimeter(sample_sides_5)
    except ValueError as e:
        print(f"Error for {sample_sides_5}: {e}")