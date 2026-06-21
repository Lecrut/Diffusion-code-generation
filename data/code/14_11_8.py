def get_third_item(data):
    try:
        return data[2]
    except IndexError:
        return None
    except TypeError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third_item(sample_list)
    print(result)
    short_list = [1, 2]
    result2 = get_third_item(short_list)
    print(result2)
    empty_list = []
    result3 = get_third_item(empty_list)
    print(result3)