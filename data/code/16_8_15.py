SAMPLE_VECTOR = [7, 14, 21, 28, 35]

def get_first_value(data):
    if len(data) == 0:
        raise IndexError("The provided vector is empty")
    return data[0]

if __name__ == '__main__':
    first_item = get_first_value(SAMPLE_VECTOR)
    print(first_item)