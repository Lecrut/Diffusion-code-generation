class ListHelper:
    @staticmethod
    def get_last_element(lst):
        return lst[-1] if lst else None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    last_element = ListHelper.get_last_element(sample_list)
    print(last_element)