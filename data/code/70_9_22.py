class ListChecker:
    def __init__(self, collection):
        self.collection = list(collection)
        self._validate()

    def _validate(self):
        if len(self.collection) == 0:
            raise ValueError("Collection cannot be empty")

    def get_first_and_last(self):
        first_element = self.collection[0]
        last_element = self.collection[-1]
        return (first_element, last_element)

if __name__ == '__main__':
    sample_values = [5, 12, 8, 23, 9]
    checker = ListChecker(sample_values)
    output = checker.get_first_and_last()
    print(output)