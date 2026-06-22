class ListProcessor:
    OFFSET_EVEN = -1
    OFFSET_ODD = 0

    @staticmethod
    def _validate_input(data):
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        if len(data) == 0:
            raise ValueError("List must not be empty")
        return True

    @staticmethod
    def find_middle(data):
        ListProcessor._validate_input(data)
        length = len(data)
        index = length // 2 + ListProcessor.OFFSET_ODD if length % 2 != 0 else length // 2 + ListProcessor.OFFSET_EVEN
        return data[index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [10, 20, 30, 40]
    single_list = [42]
    two_list = [100, 200]
    print(ListProcessor.find_middle(odd_list))
    print(ListProcessor.find_middle(even_list))
    print(ListProcessor.find_middle(single_list))
    print(ListProcessor.find_middle(two_list))