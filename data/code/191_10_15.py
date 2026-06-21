class ListCombiner:
    @staticmethod
    def extend_list(original_list, additional_items):
        original_list.extend(additional_items)
    
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    combined_list = sample_list1.copy()
    ListCombiner.extend_list(combined_list, sample_list2)
    print(combined_list)