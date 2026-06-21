THRESHOLD_X = 10
THRESHOLD_Y = 50

def evaluate_condition(x, y):
    return (x > THRESHOLD_X) and (y < THRESHOLD_Y)

if __name__ == '__main__':
    x = 13
    y = 47
    result = evaluate_condition(x, y)
    print(result)