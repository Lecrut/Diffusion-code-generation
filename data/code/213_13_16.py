class KthSmallestFinder:

    def __init__(self, numbers):
        self.numbers = numbers

    def find_kth_smallest(self, k):
        if k <= 0 or k > len(self.numbers):
            raise ValueError('k must be between 1 and the length of the list')
        for i in range(k - 1):
            min_index = i
            for j in range(i + 1, len(self.numbers)):
                if self.numbers[min_index] > self.numbers[j]:
                    min_index = j
            self.numbers[i], self.numbers[min_index] = (self.numbers[min_index], self.numbers[i])
        return self.numbers[k - 1]
if __name__ == '__main__':
    numbers = [3, 2, 9, 0, 7, 5, 6, 4, 8, 1]
    finder = KthSmallestFinder(numbers)
    k = 5
    result = finder.find_kth_smallest(k)
    print(f'The {k}-th smallest element is: {result}')