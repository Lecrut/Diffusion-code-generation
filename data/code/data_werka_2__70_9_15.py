class ListChecker:
    def __init__(self, source_list):
        self._internal_list = list(source_list)

    def get_first_and_last(self):
        if len(self._internal_list) == 0:
            raise ValueError("List is empty")
        first_element = self._internal_list[0]
        last_element = self._internal_list[-1]
        return (first_element, last_element)

if __name__ == '__main__':
    sample_values = [5, 12, 8, 19, 24]
    checker = ListChecker(sample_values)
    output = checker.get_first_and_last()
    print(output)