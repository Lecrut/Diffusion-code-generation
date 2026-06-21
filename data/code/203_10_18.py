class ListComparator:
    @staticmethod
    def is_lexicographically_smaller(list1, list2):
        len_diff = len(list1) - len(list2)
        if len_diff != 0:
            return len_diff < 0
        
        for a, b in zip(list1, list2):
            if a < b:
                return True
            elif a > b:
                return False
        
        return False

if __name__ == '__main__':
    comparator = ListComparator()
    
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    print(f"Is {sample_list1} lexicographically smaller than {sample_list2}? {comparator.is_lexicographically_smaller(sample_list1, sample_list2)}")
    
    sample_list3 = [7, 8, 9, 10]
    sample_list4 = [7, 8, 9]
    print(f"Is {sample_list3} lexicographically smaller than {sample_list4}? {comparator.is_lexicographically_smaller(sample_list3, sample_list4)}")
    
    sample_list5 = [11, 12]
    sample_list6 = [11, 12]
    print(f"Is {sample_list5} lexicographically smaller than {sample_list6}? {comparator.is_lexicographically_smaller(sample_list5, sample_list6)}")