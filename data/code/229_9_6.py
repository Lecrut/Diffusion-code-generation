def generate_square_perimeter():
    perimeter = set()
    for x in range(10):
        perimeter.add((x, 0))
        perimeter.add((x, 9))
    for y in range(1, 9):
        perimeter.add((0, y))
        perimeter.add((9, y))
    return list(perimeter)

if __name__ == '__main__':
    print(generate_square_perimeter())