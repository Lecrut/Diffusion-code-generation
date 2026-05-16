def check_equivalence(a, b, c):
    return (a == b) == (c == b)
if __name__ == '__main__':
    test_cases = [
        (10, 10, 5),
        (5, 5, 10),
        (20, 20, 15),
        (1, 1, 1),
        (3, 3, 2),
        (7, 7, 8)
    ]
    print("Equivalence Check Results:")
    for a, b, c in test_cases:
        result = check_equivalence(a, b, c)
        print(f"A={a}, B={b}, C={c}: Equivalence is {result}")