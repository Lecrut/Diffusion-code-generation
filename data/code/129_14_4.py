import heapq

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def conditional_sort(items, k, threshold):
    filtered_items = [item for item in items if item.value >= threshold]
    return heapq.nlargest(k, filtered_items, key=lambda x: x.value)

if __name__ == '__main__':
    items = [
        Item('apple', 10),
        Item('banana', 20),
        Item('cherry', 5),
        Item('date', 30)
    ]
    k = 2
    threshold = 15
    result = conditional_sort(items, k, threshold)
    print(result)