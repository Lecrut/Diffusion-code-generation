class ListChecker:
    def get_extremes(self, lst):
        if not lst:
            return None, None
        return lst[0], lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    checker = ListChecker()
    first, last = checker.get_extremes(sample_list)
    print(first, last)