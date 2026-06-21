class ListReverser:
    def __init__(self, lst):
        self.lst = lst

    def reverse(self):
        left = 0
        right = len(self.lst) - 1
        while left < right:
            self.lst[left], self.lst[right] = self.lst[right], self.lst[left]
            left += 1
            right -= 1
        return self.lst

if __name__ == '__main__':
    reverser = ListReverser([1, 2, 3, 4, 5])
    print(reverser.reverse())