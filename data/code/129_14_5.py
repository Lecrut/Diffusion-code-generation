import heapq

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def conditional_sort(items, k, threshold):
    top_k = []
    for item in items:
        if item.value >= threshold:
            heapq.heappush(top_k, (-item.value, item))
            if len(top_k) > k:
                heapq.heappop(top_k)
    return [item for _, item in sorted(top_k, key=lambda x: -x[0])]

if __name__ == '__main__':
    items = [
        Item('apple', 10),
        Item('banana', 20),
        Item('cherry', 5),
        Item('date', 15)
    ]
    k = 2
    threshold = 10
    result = conditional_sort(items, k, threshold)
    for item in result:
        print(f'{item.name}: {item.value}')