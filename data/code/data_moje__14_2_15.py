def get_third_value(data):
    if not data or len(data) < 3:
        raise IndexError("Tuple must have at least three elements")
    return data[2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_third_value(sample_tuple)
    print(result)
    try:
        get_third_value(())
    except IndexError as e:
        print(e)