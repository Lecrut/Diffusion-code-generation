def calculate_perimeter(sides):
    return sum(sides)
if __name__ == '__main__':
    sample_sides1 = [3, 4, 5]
    result1 = calculate_perimeter(sample_sides1)
    print(f"Perimeter for {sample_sides1}: {result1}")
    sample_sides2 = [10, 20, 30, 40, 50]
    result2 = calculate_perimeter(sample_sides2)
    print(f"Perimeter for {sample_sides2}: {result2}")
    sample_sides3 = [7]
    result3 = calculate_perimeter(sample_sides3)
    print(f"Perimeter for {sample_sides3}: {result3}")
    sample_sides4 = []
    result4 = calculate_perimeter(sample_sides4)
    print(f"Perimeter for {sample_sides4}: {result4}")