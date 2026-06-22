def get_last_item(lst):
    if not lst:
        return None
    return lst[-1]

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    print(get_last_item(SAMPLE_LIST))