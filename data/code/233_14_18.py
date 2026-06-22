def generate_rectangle(rows, cols, symbol):
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be greater than zero")
    
    row = symbol * cols
    return [row] * rows

if __name__ == '__main__':
    R = 5
    C = 10
    S = '*'
    rectangle = generate_rectangle(R, C, S)
    for row in rectangle:
        print(row)