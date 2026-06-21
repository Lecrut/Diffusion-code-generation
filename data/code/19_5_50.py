THRESHOLD_X = 10
THRESHOLD_Y = 50

def evaluate_conditions(x, y):
    return (x > THRESHOLD_X) and (y < THRESHOLD_Y)

if __name__ == '__main__':
    x = 25
    y = 49
    result = evaluate_conditions(x, y)
    print(result)