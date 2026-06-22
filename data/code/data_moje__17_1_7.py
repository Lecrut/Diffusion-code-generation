class ListUtils:
    def get_last_item(self, lst):
        return lst[-1]

if __name__ == '__main__':
    utils = ListUtils()
    sample_list = [10, 20, 30, 40, 50]
    result = utils.get_last_item(sample_list)
    print(result)