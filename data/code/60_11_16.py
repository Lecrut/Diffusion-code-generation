class ListHelper:
    def __init__(self, items):
        self.items = items

    def last_item(self):
        if not self.items:
            raise IndexError("Cannot retrieve last element from an empty list")
        return self.items[-1]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    helper = ListHelper(sample_list)
    print(helper.last_item())