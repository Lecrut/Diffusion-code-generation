def generate_square_perimeter(n):
    perimeter = set()
    for x in range(n):
        perimeter.add((x, 0))
        perimeter.add((x, n-1))
    for y in range(1, n-1):
        perimeter.add((0, y))
        perimeter.add((n-1, y))
    return list(perimeter)

if __name__ == '__main__':
    print(generate_square_perimeter(10))