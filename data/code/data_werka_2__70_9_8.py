class ListChecker:
    EMPTY_ERROR_MSG = "Cannot access elements of an empty list"
    
    @staticmethod
    def _validate_list(data):
        if not data:
            raise ValueError(ListChecker.EMPTY_ERROR_MSG)
        return True

    def __init__(self, data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input must be a sequence")
        self._elements = list(data)

    def get_first_and_last(self):
        self._validate_list(self._elements)
        first_item = self._elements[0]
        last_item = self._elements[-1]
        return first_item, last_item

if __name__ == '__main__':
    test_list = [11, 22, 33, 44, 55]
    checker = ListChecker(test_list)
    output = checker.get_first_and_last()
    print(output)