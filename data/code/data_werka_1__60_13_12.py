def get_last_item(lst):
    if not lst:
        return None
    return lst[-1]

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    print(get_last_item(sample_list))