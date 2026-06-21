import bisect

class SortedListSearcher:
    def __init__(self, sorted_list):
        self.sorted_list = sorted_list

    def contains_integer(self, number):
        index = bisect.bisect_left(self.sorted_list, number)
        return index < len(self.sorted_list) and self.sorted_list[index] == number

if __name__ == '__main__':
    searcher1 = SortedListSearcher([1, 2, 3, 4, 5])
    searcher2 = SortedListSearcher([-10, -5, 0, 5, 10])
    print(f"Searcher 1 contains 3: {searcher1.contains_integer(3)}")
    print(f"Searcher 1 contains 6: {searcher1.contains_integer(6)}")
    print(f"Searcher 2 contains -7: {searcher2.contains_integer(-7)}")
    print(f"Searcher 2 contains 0: {searcher2.contains_integer(0)}")