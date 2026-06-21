def get_penultimate_value(values):
    if len(values) < 2:
        raise IndexError("List must contain at least two elements")
    return values[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_penultimate_value(sample_list))
    try:
        get_penultimate_value([1])
    except IndexError as e:
        print(e)