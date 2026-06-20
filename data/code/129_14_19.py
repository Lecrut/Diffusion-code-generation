import heapq

def conditional_sort(items, k):
    return heapq.nsmallest(k, items, key=lambda x: x.value)

if __name__ == '__main__':
    class Item:
        def __init__(self, name, value):
            self.name = name
            self.value = value
    
    items = [
        Item('apple', 10),
        Item('banana', 20),
        Item('cherry', 5),
        Item('date', 15)
    ]
    
    k = 2
    result = conditional_sort(items, k)
    print(result)