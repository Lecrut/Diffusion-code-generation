class ListChecker:
    def __init__(self, container):
        self.elements = list(container)

    def get_first_and_last(self):
        total = len(self.elements)
        if total == 0:
            raise ValueError("Empty list has no first or last element")
        if total == 1:
            item = self.elements[0]
            return (item, item)
        first_item = self.elements[0]
        last_item = self.elements[-1]
        return (first_item, last_item)

if __name__ == '__main__':
    my_list = [5, 15, 25, 35, 45]
    checker_obj = ListChecker(my_list)
    output = checker_obj.get_first_and_last()
    print(output)