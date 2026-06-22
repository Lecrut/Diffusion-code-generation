class ListChecker:
    def __init__(self, container):
        self._elements = list(container)

    @staticmethod
    def _validate_non_empty(lst):
        if len(lst) == 0:
            raise ValueError("The list must not be empty")

    def get_first_and_last(self):
        self._validate_non_empty(self._elements)
        return (self._elements[0], self._elements[-1])

if __name__ == '__main__':
    my_list = ['alpha', 'beta', 'gamma', 'delta']
    checker = ListChecker(my_list)
    output = checker.get_first_and_last()
    print(output)