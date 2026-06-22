class TypeChecker:
    def all_elements_are_class_type(self, lst, cls):
        return all(isinstance(item, cls) for item in lst)

if __name__ == '__main__':
    checker = TypeChecker()
    sample_list1 = [2.5, 3.14, 42]
    result1 = checker.all_elements_are_class_type(sample_list1, float)
    print(result1)
    sample_list2 = ['apple', 'banana', 'cherry']
    result2 = checker.all_elements_are_class_type(sample_list2, str)
    print(result2)