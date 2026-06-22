def validate_triangle(a, b, c):
    return (a > 0 and b > 0 and c > 0) and (a + b > c) and (a + c > b) and (b + c > a)

def main():
    sides_a = [3, 4, 5, 1, 10, 0, -1, 5, 5, 10]
    sides_b = [4, 3, 4, 2, 10, 5, 5, 5, 1, 10]
    sides_c = [5, 5, 6, 3, 5, 0, 10, 8, 1, 20]

    results = []
    for a, b, c in zip(sides_a, sides_b, sides_c):
        results.append(validate_triangle(a, b, c))

    print(results)

if __name__ == '__main__':
    main()