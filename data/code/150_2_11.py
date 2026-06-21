class ListModifier:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def remove_all_instances(self, item):
        while item in self.items:
            index = self.items.index(item)
            del self.items[index]

if __name__ == '__main__':
    lm = ListModifier()
    lm.append(10)
    lm.append(20)
    lm.append(30)
    lm.append(20)
    print("Original list:", lm.items)
    lm.remove_all_instances(20)
    print("Modified list:", lm.items)