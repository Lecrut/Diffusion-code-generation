def both_false(x, y):
    return not (x or y)

if __name__ == '__main__':
    sample_x = None
    sample_y = []
    outcome = both_false(sample_x, sample_y)
    print(outcome)