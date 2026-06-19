class ListHandler:
    @staticmethod
    def get_first_element(data):
        return data[0] if data else None

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28]
    first_element = ListHandler.get_first_element(sample_list)
    print(first_element)