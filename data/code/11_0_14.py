class ListHelper:
    NEGATIVE_INDEX = -1

    @staticmethod
    def get_last_item(lst):
        return lst[ListHelper.NEGATIVE_INDEX]

if __name__ == '__main__':
    sample_data = [7, 14, 21, 28, 35]
    result = ListHelper.get_last_item(sample_data)
    print(result)