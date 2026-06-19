class ItemExtractor:
    SECOND_INDEX = 1

    @staticmethod
    def extract_second_item(lst):
        return lst[ItemExtractor.SECOND_INDEX]

if __name__ == '__main__':
    sample_list = [9, 18, 27, 36, 45]
    second_item = ItemExtractor.extract_second_item(sample_list)
    print(second_item)