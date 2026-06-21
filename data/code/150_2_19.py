class ListModifier:
    def __init__(self):
        self.items = []
    
    def append(self, item):
        self.items.append(item)
    
    @staticmethod
    def remove_all_instances(lst, item):
        while item in lst:
            lst.remove(item)

if __name__ == '__main__':
    lm = ListModifier()
    lm.append(1)
    lm.append(2)
    lm.append(3)
    lm.append(2)
    print("Original list:", lm.items)
    ListModifier.remove_all_instances(lm.items, 2)
    print("Modified list:", lm.items)