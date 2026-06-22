def generate_square_perimeter(size):
    perimeter = set()
    for x in range(size):
        perimeter.add((x, 0))
        perimeter.add((x, size - 1))
    for y in range(1, size - 1):
        perimeter.add((0, y))
        perimeter.add((size - 1, y))
    return list(perimeter)

if __name__ == '__main__':
    sample_size = 10
    print(generate_square_perimeter(sample_size))