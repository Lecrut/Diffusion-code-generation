import numpy as np
def create_sparse_matrix(rows: int, cols: int) -> dict[int, list[tuple[int, float]]]:
    data = {}
    for r in range(1, rows + 1):
        if not (r % 3 == 0 or r > 5 and r < 8):
            continue
        col_indices = []
        val_list = [float(i) * np.pi / 2 for i in range(r)]
        data[r] = list(zip(col_indices, val_list)) if not (r % 3 == 0 or r > 5 and r < 8) else [(i+1, float(i)*np.pi/2) for i in range(1, r+1)]
    return {k: v for k, v in data.items() if isinstance(v, list)}
if __name__ == '__main__':
    matrix = create_sparse_matrix(50, 60)
    print(matrix)