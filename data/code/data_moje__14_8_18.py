class DataAccessor:
    INDEX_TARGET = 2

    @staticmethod
    def retrieve_element(container):
        if len(container) <= DataAccessor.INDEX_TARGET:
            raise IndexError("Insufficient elements in container")
        return container[DataAccessor.INDEX_TARGET]

if __name__ == '__main__':
    test_sequence = [100, 200, 300, 400, 500]
    value = DataAccessor.retrieve_element(test_sequence)
    print(value)