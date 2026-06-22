class SetOperations:
    def find_common_elements(self, set1, set2):
        return set1.intersection(set2)

if __name__ == '__main__':
    set_ops = SetOperations()
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    print(set_ops.find_common_elements(sample_set1, sample_set2))
    
    another_set1 = {7, 8, 9}
    another_set2 = {9, 10, 11}
    print(set_ops.find_common_elements(another_set1, another_set2))