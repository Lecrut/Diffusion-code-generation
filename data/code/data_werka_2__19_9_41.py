def evaluate_condition(x, y):
    yield (x > y)
if __name__ == '__main__':
    sample_x = 15
    sample_y = 10
    gen = evaluate_condition(sample_x, sample_y)
    print(next(gen))
    print(next(gen))