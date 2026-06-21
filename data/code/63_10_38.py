class ListUtils:
    @staticmethod
    def get_first_element(lst):
        return lst[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    print(ListUtils.get_first_element(sample_list))