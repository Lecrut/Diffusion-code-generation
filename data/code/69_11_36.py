class ElementFetcher:
    def __init__(self, data_list):
        self.data_list = data_list

    def fetch_first(self):
        return self.data_list[0]

    def fetch_second(self):
        return self.data_list[1]

    def fetch_last(self):
        return self.data_list[-1]

    def fetch_penultimate(self):
        return self.data_list[-2]

    def fetch_third_last(self):
        return self.data_list[-3]

    def fetch_fourth_last(self):
        return self.data_list[-4]

    def get_elements(self):
        return {
            'first': self.fetch_first(),
            'second': self.fetch_second(),
            'last': self.fetch_last(),
            'second_last': self.fetch_penultimate(),
            'third_last': self.fetch_third_last(),
            'fourth_last': self.fetch_fourth_last()
        }

if __name__ == '__main__':
    SAMPLE_DATA = [5, 15, 25, 35, 45, 55, 65]
    fetcher = ElementFetcher(SAMPLE_DATA)
    result = fetcher.get_elements()
    print(result)