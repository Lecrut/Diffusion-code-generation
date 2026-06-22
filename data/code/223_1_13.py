def locate_maximum_value(floats):
    highest = floats[0]
    for value in floats:
        if value > highest:
            highest = value
    return highest

if __name__ == '__main__':
    numerical_samples = [3.14, 2.718, 1.618, 0.577, 1.414]
    peak_value = locate_maximum_value(numerical_samples)
    print(peak_value)