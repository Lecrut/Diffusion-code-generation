class ListHandler:
    @staticmethod
    def find_first_element(data):
        return data[0] if data else None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    first_value = ListHandler.find_first_element(sample_list)
    print(first_value)