class ListExtractor:
    INDEX_FIVE = 4

    @staticmethod
    def get_element_at_index_five(lst):
        return lst[ListExtractor.INDEX_FIVE]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45, 55]
    print(ListExtractor.get_element_at_index_five(sample_list))