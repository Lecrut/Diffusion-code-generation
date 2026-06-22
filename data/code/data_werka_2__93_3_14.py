def are_both_false(x, y):
    FALSE_VALUE = False
    return x is FALSE_VALUE and y is FALSE_VALUE

if __name__ == '__main__':
    sample_x = False
    sample_y = False
    output = are_both_false(sample_x, sample_y)
    print(output)