class ListElementRetriever:
    INDEX_OF_THIRD_ELEMENT = 2

    @staticmethod
    def retrieve_third_element(data_list):
        return data_list[ListElementRetriever.INDEX_OF_THIRD_ELEMENT]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    third_element = ListElementRetriever.retrieve_third_element(sample_data)
    print(third_element)