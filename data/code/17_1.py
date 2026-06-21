class ListHelper:
    def __init__(self, items):
        self.items = items

    def get_last_item(self):
        return self.items[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    helper = ListHelper(sample_list)
    print(helper.get_last_item())