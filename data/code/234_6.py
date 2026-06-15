def generate_checkerboard(n):
    if not isinstance(n, int) or n <= 0:
        return None
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:
                row.append('A')
            else:
                row.append('B')
        board.append(row)
    return board
if __name__ == '__main__':
    sample_inputs = [3, 4, 0, -2, 5]
    for n in sample_inputs:
        result = generate_checkerboard(n)
        print(f"Input N={n}: {result}")