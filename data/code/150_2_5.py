class ListModifier:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def remove_all_instances(self, item):
        while item in self.items:
            self.items.remove(item)

if __name__ == '__main__':
    lm = ListModifier()
    lm.append(1)
    lm.append(2)
    lm.append(3)
    lm.append(2)
    print("Original list:", lm.items)
    lm.remove_all_instances(2)
    print("Modified list:", lm.items)