class TypeValidator:
    @staticmethod
    def are_all_elements_type(lst, cls):
        return all(isinstance(item, cls) for item in lst)

if __name__ == '__main__':
    validator = TypeValidator()
    sample_list1 = [1, 2, 3]
    print(validator.are_all_elements_type(sample_list1, int))
    sample_list2 = [1, '2', 3]
    print(validator.are_all_elements_type(sample_list2, int))