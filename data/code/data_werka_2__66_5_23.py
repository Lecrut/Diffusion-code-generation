class ListChecker:
    ASCENDING = 1

    @staticmethod
    def is_sorted(lst, order=ASCENDING):
        if order == ListChecker.ASCENDING:
            return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
        raise ValueError("Unsupported order")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(ListChecker.is_sorted(sample_list))