def get_third_value(data):
    try:
        return data[2]
    except IndexError:
        raise ValueError("Tuple must contain at least three elements")

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    print(get_third_value(sample_tuple))
    try:
        get_third_value((1, 2))
    except ValueError as e:
        print(e)