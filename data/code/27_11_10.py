def check_triangle_sides(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

def main():
    side_sets = [(3, 4, 5), (1, 2, 3), (5, 5, 5), (1, 1, 10), (0, 4, 4), (7, 24, 25)]
    results = [check_triangle_sides(s) for s in side_sets]
    print(results)

if __name__ == '__main__':
    main()