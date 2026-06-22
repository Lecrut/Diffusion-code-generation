class ListAccessor:
    INDEX_OFFSET = -2

    @staticmethod
    def retrieve_element(data):
        return data[ListAccessor.INDEX_OFFSET]

if __name__ == '__main__':
    test_data = [100, 200, 300, 400, 500]
    print(ListAccessor.retrieve_element(test_data))