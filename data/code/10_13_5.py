def get_head(lst):
    if not lst:
        raise ValueError('List is empty, no head to return')
    return lst[0]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    head = get_head(sample_list)
    print(head)