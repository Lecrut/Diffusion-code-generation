class FirstItemRetriever:
    @staticmethod
    def get_first_item(data):
        return data[0]

if __name__ == '__main__':
    sample_list_1 = [42, "world", 2.718]
    first_value_1 = FirstItemRetriever.get_first_item(sample_list_1)
    print(first_value_1)

    sample_list_2 = ["banana", False, {'key': 'value'}]
    first_value_2 = FirstItemRetriever.get_first_item(sample_list_2)
    print(first_value_2)

    sample_list_3 = [None, 99, (1, 2, 3)]
    first_value_3 = FirstItemRetriever.get_first_item(sample_list_3)
    print(first_value_3)