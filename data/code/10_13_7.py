def get_list_head(lst):
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_list_head(sample_list)
    print(result)