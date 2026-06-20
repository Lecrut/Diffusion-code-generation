def evaluate_conditions(a, b, c):
    return (a >= 0 and a <= 10) and (b >= 5 and b <= 15) and (c >= 20 and c <= 30)

if __name__ == '__main__':
    print(evaluate_conditions(5, 10, 25))