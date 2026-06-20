import heapq

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def conditional_sort(items, k, threshold):
    heap = []
    for item in items:
        if item.value >= threshold:
            heapq.heappush(heap, (-item.value, item))
            if len(heap) > k:
                heapq.heappop(heap)
    return [item[1] for item in sorted(heap, key=lambda x: x[0], reverse=True)]

if __name__ == '__main__':
    items = [
        Item('apple', 5),
        Item('banana', 3),
        Item('cherry', 7),
        Item('date', 2),
        Item('elderberry', 6)
    ]
    k = 3
    threshold = 4
    sorted_items = conditional_sort(items, k, threshold)
    for item in sorted_items:
        print(f'{item.name}: {item.value}')