SYMBOL = '*'
DIMENSION = 10

def create_square_pattern(dim: int, sym: str):
    def _generate_row(row_idx: int) -> str:
        return sym * dim
    return [
        _generate_row(i)
        for i in range(dim)
    ]

if __name__ == '__main__':
    result_grid = create_square_pattern(DIMENSION, SYMBOL)
    for line in result_grid:
        print(line)