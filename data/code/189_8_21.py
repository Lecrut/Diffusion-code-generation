def remove_elements(predicate, lst):
    return [x for x in lst if not predicate(x)]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    predicate = lambda x: x % 2 != 0
    result = remove_elements(predicate, sample_list)
    print(result)