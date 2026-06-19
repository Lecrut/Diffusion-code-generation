class ListHandler:
    @staticmethod
    def get_last_item(lst):
        return lst[-1] if lst else None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    last_element = ListHandler.get_last_item(sample_list)
    print(last_element)