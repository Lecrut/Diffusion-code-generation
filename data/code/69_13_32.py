class ElementFetcher:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_first_last_middle(self):
        if not self.numbers:
            return ()
        first = self.numbers[0]
        last = self.numbers[-1]
        middle_index = len(self.numbers) // 2
        middle = self.numbers[middle_index]
        return (first, last, middle)

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    fetcher = ElementFetcher(sample_list)
    result = fetcher.get_first_last_middle()
    print(result)