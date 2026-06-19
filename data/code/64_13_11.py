class IndexFinder:
    DEFAULT_INDEX = -1

    @staticmethod
    def find_final_index(indices):
        if not indices:
            return IndexFinder.DEFAULT_INDEX
        return max(indices)

if __name__ == '__main__':
    sample_list_1 = [3, 7, 2, 9, 5]
    print(IndexFinder.find_final_index(sample_list_1))
    
    sample_list_2 = [10, 20, 30, 40, 50]
    print(IndexFinder.find_final_index(sample_list_2))
    
    sample_list_3 = []
    print(IndexFinder.find_final_index(sample_list_3))
    
    sample_list_4 = [100]
    print(IndexFinder.find_final_index(sample_list_4))