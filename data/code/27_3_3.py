def check_triangle_validity(sides):
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    return a > 0 and (a + b) > c

if __name__ == '__main__':
    samples = [
        (3, 4, 5),
        (1, 2, 3),
        (10, 10, 10),
        (0, 4, 4),
        (-1, 2, 2)
    ]
    
    results = []
    for s in samples:
        results.append(check_triangle_validity(s))
    
    for side, result in zip(samples, results):
        print(f"{side}: {result}")