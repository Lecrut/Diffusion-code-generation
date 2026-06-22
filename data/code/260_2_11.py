class SetOperations:
    def find_common_elements(self, set1, set2):
        return set1.intersection(set2)

if __name__ == '__main__':
    set_ops = SetOperations()
    
    sample_set_1 = {1, 2, 3, 4}
    sample_set_2 = {3, 4, 5, 6}
    print(set_ops.find_common_elements(sample_set_1, sample_set_2))
    
    sample_set_3 = {7, 8, 9}
    sample_set_4 = {10, 11, 12}
    print(set_ops.find_common_elements(sample_set_3, sample_set_4))