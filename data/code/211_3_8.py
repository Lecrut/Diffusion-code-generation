class SetOperations:
    SET_A = {'apple', 'banana', 'cherry'}
    SET_B = {'banana', 'cherry', 'date'}

    @staticmethod
    def get_union(set1, set2):
        return set1.union(set2)

    @staticmethod
    def get_intersection(set1, set2):
        return set1.intersection(set2)

    @staticmethod
    def get_symmetric_difference(set1, set2):
        return set1.symmetric_difference(set2)

if __name__ == '__main__':
    union_result = SetOperations.get_union(SetOperations.SET_A, SetOperations.SET_B)
    intersection_result = SetOperations.get_intersection(SetOperations.SET_A, SetOperations.SET_B)
    symmetric_difference_result = SetOperations.get_symmetric_difference(SetOperations.SET_A, SetOperations.SET_B)

    print(f"Set A: {SetOperations.SET_A}")
    print(f"Set B: {SetOperations.SET_B}")
    print(f"Union (A or B): {union_result}")
    print(f"Intersection (A and B): {intersection_result}")
    print(f"Symmetric Difference (A xor B): {symmetric_difference_result}")