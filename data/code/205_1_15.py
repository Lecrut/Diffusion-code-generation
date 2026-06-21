class DescendingSorter:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] < self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        return self.data

if __name__ == '__main__':
    sorter = DescendingSorter([3.5, 2.1, 4.8, 1.9, 5.6])
    sorted_values = sorter.sort()
    print(sorted_values)