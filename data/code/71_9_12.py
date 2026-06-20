class ListProcessor:
    @staticmethod
    def find_middle_element(lst):
        n = len(lst)
        middle_index = (n - 1) // 2
        return lst[middle_index]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1, 4]
    print(ListProcessor.find_middle_element(sample_list))
    
    sample_list_even = [1, 2, 3, 4]
    print(ListProcessor.find_middle_element(sample_list_even))
    
    sample_list_odd = [100, 200, 300]
    print(ListProcessor.find_middle_element(sample_list_odd))