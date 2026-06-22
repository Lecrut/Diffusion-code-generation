def create_checkerboard(N):
    if not isinstance(N, int) or N <= 0:
        raise ValueError("Input must be a positive integer")
    
    checkerboard = []
    for i in range(N):
        row = [1 if (i + j) % 2 == 0 else 0 for j in range(N)]
        checkerboard.append(row)
    
    return checkerboard

if __name__ == '__main__':
    n8x8 = create_checkerboard(8)
    for row in n8x8:
        print(row)