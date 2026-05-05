class ListChecker:
    def get_extremes(self, data):
        if not data:
            return None, None
        first = data[0]
        last = data[-1]
        return (first, last)
if __name__ == '__main__':
    checker = ListChecker()
    sample_list = [10, 20, 30, 40, 50]
    result = checker.get_extremes(sample_list)
    print(result)
    sample_list_two = ['a', 'b', 'c']
    result_two = checker.get_extremes(sample_list_two)
    print(result_two)
    empty_list = []
    result_empty = checker.get_extremes(empty_list)
    print(result_empty)