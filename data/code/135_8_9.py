def check_equivalence(a, b, c):
    return (a == b) and (a == c)
def structure_one(x, y, z):
    result = x
    if y > 0:
        result = x + z
    else:
        result = x - z
    return result
def structure_two(x, y, z):
    if y > 0:
        result = x + z
    else:
        result = x - z
    return result
test_cases = [
    (10, 5, 2),
    (10, -3, 2),
    (10, 0, 5),
    (10, 1, 1)
]
for x, y, z in test_cases:
    output_one = structure_one(x, y, z)
    output_two = structure_two(x, y, z)
    equivalent = check_equivalence(output_one, output_two, output_one)
    print(f"Input: ({x}, {y}, {z})")
    print(f"Structure One Output: {output_one}")
    print(f"Structure Two Output: {output_two}")
    print(f"Equivalence Check: {equivalent}")
    print("-" * 20)
if __name__ == '__main__':
    pass