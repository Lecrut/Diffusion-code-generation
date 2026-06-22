class TypeChecker:
    @staticmethod
    def all_elements_are_class_type(lst, cls):
        return all(isinstance(item, cls) for item in lst)

if __name__ == '__main__':
    checker = TypeChecker()
    sample_list1 = [1, 2, 3]
    print(checker.all_elements_are_class_type(sample_list1, int))
    sample_list2 = [1, '2', 3]
    print(checker.all_elements_are_class_type(sample_list2, int))