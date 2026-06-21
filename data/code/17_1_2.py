class ListHelper:
    def get_last_item(self, lst):
        if not lst:
            raise IndexError("List is empty")
        return lst[-1]

if __name__ == '__main__':
    helper = ListHelper()
    sample_list = [1, 2, 3, 4, 5]
    result = helper.get_last_item(sample_list)
    print(result)