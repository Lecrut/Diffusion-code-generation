class FirstElementRetriever:
    DEFAULT_VALUE = None

    @staticmethod
    def get_first_element(data):
        if not data:
            return FirstElementRetriever.DEFAULT_VALUE
        return data[0]

if __name__ == '__main__':
    sample1 = [7, 8, 9]
    sample2 = ['x', 'y', 'z']
    empty_list = []
    single_item = [3.14]
    print(f"First element of {sample1}: {FirstElementRetriever.get_first_element(sample1)}")
    print(f"First element of {sample2}: {FirstElementRetriever.get_first_element(sample2)}")
    print(f"First element of {empty_list}: {FirstElementRetriever.get_first_element(empty_list)}")
    print(f"First element of {single_item}: {FirstElementRetriever.get_first_element(single_item)}")