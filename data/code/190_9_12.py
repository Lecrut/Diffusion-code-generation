import bisect

class SortedListSearcher:
    @staticmethod
    def contains_number(sorted_list, target):
        index = bisect.bisect_left(sorted_list, target)
        return index != len(sorted_list) and sorted_list[index] == target

if __name__ == '__main__':
    searcher = SortedListSearcher()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50]
    print(f"Number 3 is in list1: {searcher.contains_number(list1, 3)}")
    print(f"Number 6 is in list2: {searcher.contains_number(list2, 6)}")