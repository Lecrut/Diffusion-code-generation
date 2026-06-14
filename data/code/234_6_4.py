def generate_checkerboard(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input: N must be a positive integer."
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:
                row.append(" ")
            else:
                row.append("X")
        board.append(row)
    return board
if __name__ == '__main__':
    sample_inputs = [4, 0, -2, 3]
    for n in sample_inputs:
        result = generate_checkerboard(n)
        print(f"Input N={n}:")
        if isinstance(result, list):
            for row in result:
                print("".join(row))
        else:
            print(result)
        print("-" * 10)