class FirstItemRetriever:
    @staticmethod
    def get_first_item(data):
        return data[0]

if __name__ == '__main__':
    sample_values = [
        [42, "world", 7.89],
        ["apple", 123, None],
        [True, False],
        [[1, 2], [3, 4]],
        {"key": "value"},
        (5, 6, 7)
    ]

    for value in sample_values:
        first_item = FirstItemRetriever.get_first_item(value)
        print(first_item)