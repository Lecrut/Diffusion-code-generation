def evaluate_condition(x, y):
    if x > y:
        yield True
    else:
        yield False
if __name__ == '__main__':
    for x_val, y_val in [(5, 3), (1, 10), (7, 7), (0, -2)]:
        print(f"x={x_val}, y={y_val}: ", end="")
        result = False
        for item in evaluate_condition(x_val, y_val):
            result = item
        print(f"Result: {result}")