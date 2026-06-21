def remove_elements(predicate, lst):
    return [item for item in lst if not predicate(item)]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    predicate = lambda x: x % 2 == 0
    result = remove_elements(predicate, sample_list)
    print(result)