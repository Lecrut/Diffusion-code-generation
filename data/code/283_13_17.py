class TypeChecker:
    def all_elements_are_class_type(self, lst, cls):
        if not isinstance(lst, list):
            raise ValueError('The first argument must be a list.')
        if not isinstance(cls, type):
            raise ValueError('The second argument must be a class type.')
        return all(isinstance(item, cls) for item in lst)

if __name__ == '__main__':
    checker = TypeChecker()
    sample_list1 = [1, 2, 3]
    print(checker.all_elements_are_class_type(sample_list1, int))
    sample_list2 = [1, '2', 3]
    try:
        print(checker.all_elements_are_class_type(sample_list2, int))
    except ValueError as e:
        print(e)
    sample_list3 = ['a', 'b', 'c']
    try:
        print(checker.all_elements_are_class_type(sample_list3, str))
    except ValueError as e:
        print(e)