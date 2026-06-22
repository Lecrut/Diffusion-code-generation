class ListExtender:

    def __init__(self, initial_list):
        self.list = initial_list

    def extend_with_last_element(self, n):
        if not self.list or n <= 0:
            return
        last_element = self.list[-1]
        self.list.extend([last_element] * n)
if __name__ == '__main__':
    extender = ListExtender([1, 2, 3])
    extender.extend_with_last_element(3)
    print(extender.list)