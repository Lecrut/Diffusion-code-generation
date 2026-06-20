def flip_boolean(value):
    bool_map = {True: False, False: True}
    return bool_map[value]

if __name__ == '__main__':
    sample_value = True
    print(flip_boolean(sample_value))
    another_sample = False
    print(flip_boolean(another_sample))