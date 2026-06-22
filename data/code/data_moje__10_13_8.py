def get_head(lst):
    if not lst:
        raise IndexError("Cannot get head of an empty list")
    return lst[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    print(get_head(sample_list))