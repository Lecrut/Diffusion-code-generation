class ListHelper:
    DEFAULT_INDEX = -1

    @staticmethod
    def fetch_tail(sequence):
        return sequence[ListHelper.DEFAULT_INDEX]

if __name__ == '__main__':
    data_set = [100, 200, 300, 400, 500]
    output = ListHelper.fetch_tail(data_set)
    print(output)