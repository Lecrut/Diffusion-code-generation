def get_middle_value(data):
    MIDPOINT_OFFSET = 2
    LENGTH_MULTIPLIER = 2
    index = (len(data) + MIDPOINT_OFFSET) // LENGTH_MULTIPLIER
    return data[index]

if __name__ == '__main__':
    sample_data = [11, 22, 33, 44, 55]
    value = get_middle_value(sample_data)
    print(value)