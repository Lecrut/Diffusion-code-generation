class ListReverser:
    def __init__(self, data):
        self.data = data

    def reverse_with_swap(self):
        left = 0
        right = len(self.data) - 1
        while left < right:
            self.data[left], self.data[right] = self.data[right], self.data[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    reverser.reverse_with_swap()
    print(reverser.data)