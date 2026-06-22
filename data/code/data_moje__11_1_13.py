def safe_pop_last(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    empty_list = []
    print(safe_pop_last(sample_list))
    print(safe_pop_last(sample_list))
    print(safe_pop_last(sample_list))
    print(safe_pop_last(empty_list))
    print(safe_pop_last(empty_list))