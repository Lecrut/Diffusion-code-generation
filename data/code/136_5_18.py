def evaluate_expression(x, y, z):
    return (x < y) and not (y > z)

if __name__ == '__main__':
    result = evaluate_expression(3, 5, 2)
    print(result)