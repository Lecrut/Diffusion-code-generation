import heapq

class Item:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

def conditional_sort(items, k):
    if k >= len(items):
        return sorted(items, key=lambda x: x.priority)
    else:
        return heapq.nsmallest(k, items, key=lambda x: x.priority)

if __name__ == '__main__':
    items = [Item('a', 3), Item('b', 1), Item('c', 2)]
    k = 2
    sorted_items = conditional_sort(items, k)
    print([(item.value, item.priority) for item in sorted_items])