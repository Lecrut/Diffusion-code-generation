any_truthy = lambda lst: any(lst)
if __name__ == '__main__':
    sample_list1 = [0, False, None, '']
    sample_list2 = [0, False, None, 'hello']
    print(any_truthy(sample_list1))
    print(any_truthy(sample_list2))