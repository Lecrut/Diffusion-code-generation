class ListChecker:
    def __init__(self, source_list):
        self._elements = list(source_list)
    def get_first_and_last(self):
        num_items = len(self._elements)
        if num_items == 0:
            raise ValueError("List is empty")
        first_element = self._elements[0]
        last_element = self._elements[-1]
        return (first_element, last_element)
if __name__ == '__main__':
    sample_values = [7, 14, 21, 28, 35]
    my_checker = ListChecker(sample_values)
    output = my_checker.get_first_and_last()
    print(output)