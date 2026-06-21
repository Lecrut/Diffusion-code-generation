import heapq

class SmallestElementFinder:
    def __init__(self, data):
        self.data = data
    
    def find_smallest(self):
        return heapq.nsmallest(1, self.data)[0]

if __name__ == '__main__':
    finder = SmallestElementFinder([3.5, 2.1, 4.8, 1.9, 5.6])
    smallest_number = finder.find_smallest()
    print(smallest_number)