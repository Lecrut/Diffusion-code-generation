def check_equivalence(a, b, c):
    return (a == b) and (a == c)
def structure_one(x, y):
    result = x if x > y else y
    return result
def structure_two(x, y):
    result = x
    if y > x:
        result = y
    return result
if __name__ == '__main__':
    test_cases = [
        (5, 3, 3),
        (10, 2, 2),
        (7, 7, 7),
        (1, 5, 5),
        (8, 4, 4)
    ]
    print("Equivalence Check Demonstration:")
    for x, y, z in test_cases:
        output_one = structure_one(x, y)
        output_two = structure_two(x, y)
        equivalent = check_equivalence(output_one, output_two, x)
        print(f"Test Case (x={x}, y={y}, z={z}):")
        print(f"Structure One Result: {output_one}")
        print(f"Structure Two Result: {output_two}")
        print(f"Are results equivalent (and equal to x)? {equivalent}")
        print("-" * 20)