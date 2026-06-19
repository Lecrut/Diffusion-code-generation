class IndexFinder:
    EMPTY_LIST_RETURN = -1

    @staticmethod
    def find_final_index(indices):
        if not indices:
            return IndexFinder.EMPTY_LIST_RETURN
        return max(indices)

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5]
    print(IndexFinder.find_final_index(sample_list1))
    
    sample_list2 = [9, 8, 7, 6, 5]
    print(IndexFinder.find_final_index(sample_list2))
    
    sample_list3 = []
    print(IndexFinder.find_final_index(sample_list3))
    
    sample_list4 = [0, -1, -2, -3]
    print(IndexFinder.find_final_index(sample_list4))