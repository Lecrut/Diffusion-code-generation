class ListHandler:
    DEFAULT_VALUE = None

    @staticmethod
    def get_first_element(data):
        return data[0] if data else ListHandler.DEFAULT_VALUE

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    first_value = ListHandler.get_first_element(sample_list)
    print(first_value)