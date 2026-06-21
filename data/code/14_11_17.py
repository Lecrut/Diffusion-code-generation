def get_third_item(lst):
    try:
        return lst[2]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_third_item(sample_list)
    print(result)