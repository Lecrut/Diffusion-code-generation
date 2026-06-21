class ListAccessor:
    def get_last_item(self, lst):
        if not lst:
            return None
        return lst[len(lst) - 1]

if __name__ == '__main__':
    accessor = ListAccessor()
    sample_list = [10, 20, 30, 40]
    result = accessor.get_last_item(sample_list)
    print(result)