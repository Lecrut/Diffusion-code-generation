import heapq

class ListMerger:
    def merge_sorted_lists(self, list1, list2):
        return list(heapq.merge(list1, list2))

if __name__ == '__main__':
    merger = ListMerger()
    
    list_a = [1, 3, 5]
    list_b = [2, 4, 6]
    result1 = merger.merge_sorted_lists(list_a, list_b)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Merged List: {result1}")
    
    list_c = ['apple', 'cherry', 'elderberry']
    list_d = ['banana', 'date', 'fig']
    result2 = merger.merge_sorted_lists(list_c, list_d)
    print(f"List C: {list_c}")
    print(f"List D: {list_d}")
    print(f"Merged List: {result2}")