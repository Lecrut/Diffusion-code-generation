def get_last_item(lst):
    try:
        return lst[-1]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_item(sample_list))