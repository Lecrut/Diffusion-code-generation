def get_last_item(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_item(sample_list))
    print(get_last_item([]))