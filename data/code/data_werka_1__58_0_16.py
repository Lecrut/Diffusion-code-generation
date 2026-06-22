class ListHandler:
    DEFAULT_LIST = [100, 200, 300, 400]

    @staticmethod
    def retrieve_first_element(data_list):
        return data_list[0] if data_list else None

if __name__ == '__main__':
    sample_list = ListHandler.DEFAULT_LIST
    first_element = ListHandler.retrieve_first_element(sample_list)
    print(first_element)