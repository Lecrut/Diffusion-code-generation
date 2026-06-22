class LastElementFetcher:
    INDEX_NEGATIVE_ONE = -1

    @staticmethod
    def get_last(data: list):
        return data[LastElementFetcher.INDEX_NEGATIVE_ONE]

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    print(LastElementFetcher.get_last(sample_data))