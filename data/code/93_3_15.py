def both_false(x, y):
    is_x_false = not bool(x)
    is_y_false = not bool(y)
    return is_x_false and is_y_false

if __name__ == '__main__':
    sample_x = None
    sample_y = []
    result = both_false(sample_x, sample_y)
    print(result)