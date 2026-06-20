THRESHOLD_X = 5
THRESHOLD_Y = 10

def combine_conditions(x, y):
    return x > THRESHOLD_X and y < THRESHOLD_Y

if __name__ == '__main__':
    sample_x = 6
    sample_y = 8
    result = combine_conditions(sample_x, sample_y)
    print(result)