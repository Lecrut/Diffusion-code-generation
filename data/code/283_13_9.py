class TypeChecker:
    def all_elements_are_class_type(self, lst, cls):
        return all(isinstance(item, cls) for item in lst)

if __name__ == '__main__':
    checker = TypeChecker()
    sample_list1 = [2.0, 3.5, 4.7]
    print(checker.all_elements_are_class_type(sample_list1, float))
    sample_list2 = [2.0, '3.5', 4.7]
    print(checker.all_elements_are_class_type(sample_list2, float))