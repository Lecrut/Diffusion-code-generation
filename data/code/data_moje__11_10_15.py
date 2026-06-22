class LastElementRetriever:
    INDEX_OFFSET = -1

    @staticmethod
    def get_last(data):
        return data[LastElementRetriever.INDEX_OFFSET]

if __name__ == '__main__':
    sample_data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    value = LastElementRetriever.get_last(sample_data)
    print(value)