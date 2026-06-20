a = True
b = False

def evaluate_condition(x, y):
    return x and y

if __name__ == '__main__':
    result = evaluate_condition(a, b)
    print(result)