def get_last_item(lst):
    return lst[-1] if lst else None

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    print(get_last_item(SAMPLE_LIST))