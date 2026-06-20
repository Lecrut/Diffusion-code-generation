def evaluate_logic(a, b):
    return a & b

if __name__ == '__main__':
    x = False
    y = True
    result = evaluate_logic(x, y)
    print(result)