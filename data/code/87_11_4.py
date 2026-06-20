def evaluate_conditions(x, y):
    return x > 5 and y < 10

if __name__ == '__main__':
    sample_x = 6
    sample_y = 8
    result = evaluate_conditions(sample_x, sample_y)
    print(result)