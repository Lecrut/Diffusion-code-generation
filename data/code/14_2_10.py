def get_third_value(data_tuple):
    if len(data_tuple) < 3:
        raise ValueError("Tuple must contain at least three elements")
    return data_tuple[2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    print(get_third_value(sample_tuple))