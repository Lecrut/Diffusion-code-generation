class ItemRetriever:
    EMPTY_SENTINEL = None

    @staticmethod
    def get_last_value(container):
        current_value = ItemRetriever.EMPTY_SENTINEL
        for element in container:
            current_value = element
        return current_value

if __name__ == '__main__':
    test_sequence = [100, 200, 300, 400, 500]
    print(ItemRetriever.get_last_value(test_sequence))