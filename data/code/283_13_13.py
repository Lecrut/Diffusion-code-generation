class TypeValidator:
    def all_elements_are_type(self, lst, target_type):
        return all(isinstance(item, target_type) for item in lst)

if __name__ == '__main__':
    validator = TypeValidator()
    sample_list1 = [1, 2, 3]
    print(validator.all_elements_are_type(sample_list1, int))
    sample_list2 = [1, '2', 3]
    print(validator.all_elements_are_type(sample_list2, int))