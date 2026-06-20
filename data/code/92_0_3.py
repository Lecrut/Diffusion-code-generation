def toggle_boolean(value):
    return not value

if __name__ == '__main__':
    sample_value = True
    opposite_value = toggle_boolean(sample_value)
    print(opposite_value)

    another_sample = False
    another_opposite = toggle_boolean(another_sample)
    print(another_opposite)