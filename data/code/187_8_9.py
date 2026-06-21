class LargestElementFinder:
    def __init__(self, data):
        self.data = data

    def find_largest(self):
        if not self.data:
            return None
        largest = self.data[0]
        for i in range(1, len(self.data)):
            if self.data[i] > largest:
                largest = self.data[i]
        return largest

if __name__ == '__main__':
    finder1 = LargestElementFinder([3, 1, 4, 1, 5, 9, 2])
    print(f"List: [3, 1, 4, 1, 5, 9, 2], Largest element: {finder1.find_largest()}")

    finder2 = LargestElementFinder([-10, -5, -20, -1])
    print(f"List: [-10, -5, -20, -1], Largest element: {finder2.find_largest()}")

    finder3 = LargestElementFinder([7])
    print(f"List: [7], Largest element: {finder3.find_largest()}")

    finder4 = LargestElementFinder([])
    print(f"List: [], Largest element: {finder4.find_largest()}")