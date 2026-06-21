class ListConcatenator:
    def __init__(self, list1, list2):
        self.list1 = iter(list1)
        self.list2 = iter(list2)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.list1)
        except StopIteration:
            return next(self.list2)

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenator = ListConcatenator(list1, list2)
    result = [item for item in concatenator]
    print(f"Concatenated list: {result}")