def generate_square_perimeter(n):
    perimeter = set()
    for i in range(n):
        perimeter.add((i, 0))
        perimeter.add((n-1, i))
        perimeter.add((i, n-1))
        perimeter.add((0, i))
    return list(perimeter)

if __name__ == '__main__':
    sample_perimeter = generate_square_perimeter(10)
    print(sample_perimeter)