def generate_square_perimeter(N):
    if not isinstance(N, int) or N <= 0:
        raise ValueError("N must be a positive integer")
    
    perimeter = set()
    for i in range(N):
        perimeter.add((i, 0))
        perimeter.add((i, N-1))
        perimeter.add((0, i))
        perimeter.add((N-1, i))
    
    return list(perimeter)

if __name__ == '__main__':
    N_sample = 10
    perimeter_points = generate_square_perimeter(N_sample)
    print(perimeter_points)