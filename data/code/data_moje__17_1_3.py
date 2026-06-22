class ListHelper:
    def __init__(self, data):
        self.data = data

    def get_last_item(self):
        return self.data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    helper = ListHelper(sample_list)
    print(helper.get_last_item())