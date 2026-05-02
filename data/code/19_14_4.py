def evaluate_condition(x, y):
    if x > y:
        yield True
    else:
        yield False
if __name__ == '__main__':
    for x_val, y_val in [(5, 3), (1, 10), (7, 7), (2, 9)]:
        print(f"x={x_val}, y={y_val}: ", end="")
        result = list(evaluate_condition(x_val, y_val))[0]
        print(f"Result: {result}")