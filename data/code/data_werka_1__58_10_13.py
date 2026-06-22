class ListAccessor:
    @staticmethod
    def get_first_element(lst):
        return lst[0] if lst else None

if __name__ == '__main__':
    sample_list = [15, 30, 45]
    print(ListAccessor.get_first_element(sample_list))