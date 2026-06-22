def validate_integers(x, y):
    if type(x) is not int or type(y) is not int:
        raise ValueError("Both inputs must be integers")
    return True

def is_x_greater_than_y(x, y):
    validate_integers(x, y)
    return x > y

if __name__ == '__main__':
    sample_x = 10
    sample_y = 5
    result = is_x_greater_than_y(sample_x, sample_y)
    print(result)