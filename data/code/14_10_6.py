class ListElementRetriever:
    REQUIRED_LENGTH = 3
    TARGET_INDEX = 2

    @staticmethod
    def get_third_element(data):
        if len(data) < ListElementRetriever.REQUIRED_LENGTH:
            raise IndexError("List does not contain a third element")
        return data[ListElementRetriever.TARGET_INDEX]

if __name__ == '__main__':
    test_values = ["alpha", "beta", "gamma", "delta", "epsilon"]
    extracted_value = ListElementRetriever.get_third_element(test_values)
    print(extracted_value)