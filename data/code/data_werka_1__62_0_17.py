class ListAccessor:
    INDEX_SECOND_ITEM = 1

    @staticmethod
    def get_second_item(lst):
        return lst[ListAccessor.INDEX_SECOND_ITEM]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    second_item = ListAccessor.get_second_item(sample_list)
    print(second_item)