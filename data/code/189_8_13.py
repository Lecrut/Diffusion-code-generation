def remove_elements(lst, predicate):
    return [x for x in lst if not predicate(x)]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    predicate_function = lambda x: x % 2 == 0
    filtered_list = remove_elements(sample_list, predicate_function)
    print(filtered_list)