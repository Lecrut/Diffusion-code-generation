class ListChecker:
    def get_extremes(self, lst):
        if not lst:
            return None
        return (lst[0], lst[-1])

if __name__ == '__main__':
    checker = ListChecker()
    sample_list = [1, 2, 3, 4, 5]
    print(checker.get_extremes(sample_list))