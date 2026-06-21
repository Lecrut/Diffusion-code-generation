class ListExtender:
    def __init__(self, base_list):
        self.base_list = base_list

    def extend(self, extension_list):
        for item in extension_list:
            if item not in self.base_list:
                self.base_list.append(item)

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    extender = ListExtender(list_a)
    extender.extend(list_b)
    print(extender.base_list)