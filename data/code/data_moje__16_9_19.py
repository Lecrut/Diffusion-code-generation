class ElementRetriever:
    DEFAULT_EMPTY_VALUE = None

    @staticmethod
    def get_first_element(lst):
        if len(lst) == 0:
            return ElementRetriever.DEFAULT_EMPTY_VALUE
        first_item = lst[0]
        return first_item

if __name__ == '__main__':
    numbers = [100, 200, 300]
    empty_numbers = []
    result_one = ElementRetriever.get_first_element(numbers)
    result_two = ElementRetriever.get_first_element(empty_numbers)
    print(result_one)
    print(result_two)