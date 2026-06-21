class ListAccessor:
    class Indices:
        LAST = -1

    @staticmethod
    def get_last(lst):
        return lst[ListAccessor.Indices.LAST]

if __name__ == '__main__':
    test_data = [100, 200, 300, 400, 500]
    print(ListAccessor.get_last(test_data))