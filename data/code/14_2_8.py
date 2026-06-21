def get_third_value(data: tuple) -> any:
    if len(data) < 3:
        raise IndexError("Tuple must contain at least three elements")
    return data[2]

if __name__ == "__main__":
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_third_value(sample_tuple)
    print(result)

    empty_tuple = ()
    try:
        get_third_value(empty_tuple)
    except IndexError as e:
        print(str(e))