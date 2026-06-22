class TypeChecker:
    def all_elements_are_class_type(self, lst, cls):
        return all(isinstance(item, cls) for item in lst)

if __name__ == '__main__':
    checker = TypeChecker()
    sample_list1 = [42, 3.14, 'hello']
    print(checker.all_elements_are_class_type(sample_list1, int))
    sample_list2 = [42, 3.14]
    print(checker.all_elements_are_class_type(sample_list2, (int, float)))