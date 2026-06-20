class ListChecker:
    @staticmethod
    def get_first_and_last(lst):
        if not lst:
            raise ValueError("List is empty")
        return lst[0], lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        first, last = ListChecker.get_first_and_last(sample_list)
        print(f"First item: {first}")
        print(f"Last item: {last}")
    except ValueError as e:
        print(e)