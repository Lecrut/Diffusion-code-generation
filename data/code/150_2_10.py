class ListModifier:
    DEFAULT_LIST = []

    def __init__(self):
        self.items = self.DEFAULT_LIST.copy()

    def append(self, item):
        self.items.append(item)

    @classmethod
    def remove_all_instances(cls, lst, value):
        while value in lst:
            lst.remove(value)

if __name__ == '__main__':
    lm = ListModifier()
    lm.append(1)
    lm.append(2)
    lm.append(3)
    lm.append(2)
    print("Original list:", lm.items)
    ListModifier.remove_all_instances(lm.items, 2)
    print("Modified list:", lm.items)