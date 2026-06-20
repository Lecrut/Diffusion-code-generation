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
        return heapq.nsmallest(k, items)

if __name__ == '__main__':
    items = [Item('a', 3), Item('b', 1), Item('c', 2)]
    top_k = conditional_sort(items, 2)
    print([(item.value, item.priority) for item in top_k])