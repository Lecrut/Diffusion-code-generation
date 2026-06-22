SYMBOL = '*'
ROWS = 5
COLUMNS = 4

def create_symbol_matrix(rows=ROWS, columns=COLUMNS, symbol=SYMBOL):
    matrix = []
    for _ in range(rows):
        row = [symbol] * columns
        matrix.append(row)
    return matrix

if __name__ == '__main__':
    result = create_symbol_matrix()
    print(result)