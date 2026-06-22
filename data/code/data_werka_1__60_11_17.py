class ListHelper:
    @staticmethod
    def get_last_element(lst):
        if not lst:
            raise IndexError("Cannot retrieve last element from an empty list")
        return lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    last_element = ListHelper.get_last_element(sample_list)
    print(last_element)