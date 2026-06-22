def generate_square_perimeter(N):
    perimeter = set()
    for i in range(N):
        perimeter.add((i, 0))
        perimeter.add((i, N-1))
    for j in range(1, N-1):
        perimeter.add((0, j))
        perimeter.add((N-1, j))
    return list(perimeter)

if __name__ == '__main__':
    N_sample = 10
    perimeter_coords = generate_square_perimeter(N_sample)
    print(perimeter_coords)