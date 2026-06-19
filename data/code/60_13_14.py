def get_last_item(lst):
    return lst[-1] if lst else None

if __name__ == '__main__':
    SAMPLE_LIST = [100, 200, 300, 400, 500]
    print(get_last_item(SAMPLE_LIST))