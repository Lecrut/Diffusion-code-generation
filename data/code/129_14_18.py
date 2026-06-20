import heapq

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def conditional_sort(items, k, threshold):
    top_k_items = []
    for item in items:
        if item.value >= threshold:
            heapq.heappush(top_k_items, (-item.value, item))
            if len(top_k_items) > k:
                heapq.heappop(top_k_items)
    return [item[1] for item in sorted(top_k_items, key=lambda x: -x[0])]

if __name__ == '__main__':
    items = [
        Item('apple', 5),
        Item('banana', 3),
        Item('cherry', 8),
        Item('date', 2),
        Item('elderberry', 7)
    ]
    k = 3
    threshold = 4
    result = conditional_sort(items, k, threshold)
    for item in result:
        print(f'{item.name}: {item.value}')