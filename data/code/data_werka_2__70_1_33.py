class ListChecker:
    SUPPORTED_CONTAINER_TYPES = (list, tuple)
    EMPTY_LIST_ERROR = "Collection cannot be empty"
    TYPE_ERROR = "Unsupported input type"

    def get_extremes(self, collection):
        if not isinstance(collection, self.SUPPORTED_CONTAINER_TYPES):
            raise ValueError(self.TYPE_ERROR)
        if len(collection) == 0:
            raise ValueError(self.EMPTY_LIST_ERROR)
        first = collection[0]
        last = collection[-1]
        return (first, last)

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    checker = ListChecker()
    extremes = checker.get_extremes(numbers)
    print(extremes)