THRESHOLD_X = 5
THRESHOLD_Y = 10

def check_conditions(x, y):
    return x > THRESHOLD_X and y < THRESHOLD_Y

if __name__ == '__main__':
    result = check_conditions(6, 8)
    print(result)