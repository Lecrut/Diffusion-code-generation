def pop_last(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = pop_last(sample_list)
    print(result)
    
    empty_list = []
    result_empty = pop_last(empty_list)
    print(result_empty)