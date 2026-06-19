class ListHandler:
    @staticmethod
    def find_last_element(data):
        if not data:
            return None
        return data[-1]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    last_element = ListHandler.find_last_element(sample_list)
    print(last_element)