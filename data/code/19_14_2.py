def evaluate_condition(x, y):
    if x > y:
        yield True
    else:
        yield False
if __name__ == '__main__':
    for x_val, y_val in [(5, 3), (2, 8), (10, 10), (1, 0)]:
        print(f"x={x_val}, y={y_val}: ", end="")
        for result in evaluate_condition(x_val, y_val):
            print(result, end=" ")
        print()