import heapq

class HeapSorter:
    def __init__(self):
        self.heap = []

    def add_number(self, number):
        heapq.heappush(self.heap, number)

    def sort_numbers(self):
        return [heapq.heappop(self.heap) for _ in range(len(self.heap))]

if __name__ == '__main__':
    sorter = HeapSorter()
    sample_values = [5, 3, 8, 1, 2]
    for value in sample_values:
        sorter.add_number(value)
    sorted_values = sorter.sort_numbers()
    print(sorted_values)