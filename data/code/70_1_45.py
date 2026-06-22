class ListChecker:
    FIRST_INDEX = 0
    LAST_INDEX = -1

    def get_extremes(self, collection):
        if len(collection) == 0:
            raise ValueError("Collection cannot be empty")
        return (collection[self.FIRST_INDEX], collection[self.LAST_INDEX])

if __name__ == '__main__':
    data = [42, 17, 99, 3, 8]
    tool = ListChecker()
    print(tool.get_extremes(data))