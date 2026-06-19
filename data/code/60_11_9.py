class ListHelper:
    @staticmethod
    def get_last_element(lst):
        return lst[-1]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    last_item = ListHelper.get_last_element(sample_list)
    print(last_item)