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
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    reversed_list = reverser.reverse()
    print(reversed_list)

    another_sample_list = [7, 8, 9, 10, 11]
    another_reverser = ListReverser(another_sample_list)
    another_reversed_list = another_reverser.reverse()
    print(another_reversed_list)