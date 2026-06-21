class NumberFilter:
    def filter_odds(self, numbers):
        return list(filter(lambda x: x % 2 != 0, numbers))

if __name__ == '__main__':
    filter_instance = NumberFilter()
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_instance.filter_odds(sample_list)
    print(result)