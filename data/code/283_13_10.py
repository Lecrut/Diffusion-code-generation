class TypeValidator:
    @staticmethod
    def all_elements_are_instance(lst, cls):
        return all(isinstance(item, cls) for item in lst)

if __name__ == '__main__':
    validator = TypeValidator()
    sample_list1 = [1, 2, 3]
    print(validator.all_elements_are_instance(sample_list1, int))
    sample_list2 = [1, '2', 3]
    print(validator.all_elements_are_instance(sample_list2, int))