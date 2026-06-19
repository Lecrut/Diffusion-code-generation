class ListHandler:
    INDEX_SECOND = 1

    @staticmethod
    def extract_second_item(lst):
        return lst[ListHandler.INDEX_SECOND]

if __name__ == '__main__':
    sample_list = [9, 18, 27, 36, 45]
    second_item = ListHandler.extract_second_item(sample_list)
    print(second_item)