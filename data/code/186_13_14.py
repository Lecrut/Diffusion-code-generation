class ListReverser:
    def __init__(self, lst):
        self.lst = lst

    def reverse_in_place(self):
        left, right = 0, len(self.lst) - 1
        while left < right:
            self.lst[left], self.lst[right] = self.lst[right], self.lst[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    reverser = ListReverser([10, 20, 30, 40, 50])
    reverser.reverse_in_place()
    print(reverser.lst)