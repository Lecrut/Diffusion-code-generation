class ListChecker:
    def __init__(self):
        self.supported_types = {
            list: True,
            tuple: True,
            str: True
        }

    def get_extremes(self, lst):
        if not isinstance(lst, (list, tuple)):
            raise ValueError("Unsupported type")
        if not lst:
            raise ValueError("The list is empty")
        return (lst[0], lst[-1])

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    checker = ListChecker()
    print(checker.get_extremes(sample_list))