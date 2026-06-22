def get_last_item(lst):
    if not lst:
        return None
    return lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_item(sample_list))