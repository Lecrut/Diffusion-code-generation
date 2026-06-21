class ListUtils:
    def second_to_last(self, data):
        return data[-2]

    def last(self, data):
        return data[-1]

if __name__ == '__main__':
    utils = ListUtils()
    items = [5, 10, 15, 20, 25]
    print(utils.second_to_last(items))
    print(utils.last(items))