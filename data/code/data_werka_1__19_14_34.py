if __name__ == '__main__':
    sample_list_1 = [0, False, None, '']
    sample_list_2 = [0, False, None, 'hello']
    contains_truthy = lambda lst: any(lst)
    print(contains_truthy(sample_list_1))
    print(contains_truthy(sample_list_2))