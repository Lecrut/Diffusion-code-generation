def check_equivalence(a, b, c):
    return (a == b) and (a == c)
def structure_one(x, y):
    result = x
    if y > 10:
        result = x + 1
    else:
        result = x + 2
    return result
def structure_two(x, y):
    result = x
    if y < 10:
        result = x + 1
    else:
        result = x + 2
    return result
test_cases = [
    (5, 5, 5),
    (12, 12, 12),
    (8, 8, 8),
    (15, 15, 15),
    (3, 1, 3)
]
print("Equivalence Checking Results:")
for x, y, z in test_cases:
    output1 = structure_one(x, y)
    output2 = structure_two(x, y)
    is_equivalent = check_equivalence(output1, output2, x)
    print(f"Input (x={x}, y={y}): Output1={output1}, Output2={output2}, Equivalent={is_equivalent}")
if __name__ == '__main__':
    pass