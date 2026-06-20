def evaluate_logic(a, b):
    return a & b

if __name__ == '__main__':
    x = True
    y = False
    result = evaluate_logic(x, y)
    print(result)