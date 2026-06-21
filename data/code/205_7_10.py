import heapq

class HeapSorter:
    def __init__(self, numbers):
        self.numbers = numbers

    def sort(self):
        heapq.heapify(self.numbers)
        return [heapq.heappop(self.numbers) for _ in range(len(self.numbers))]

if __name__ == '__main__':
    sorter = HeapSorter([5, 3, 8, 1, 2])
    sorted_values = sorter.sort()
    print(sorted_values)