def remove_elements(lst, predicate):
    return [x for x in lst if not predicate(x)]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    predicate = lambda x: x % 2 == 0
    result = remove_elements(sample_list, predicate)
    print(result)