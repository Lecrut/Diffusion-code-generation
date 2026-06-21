class ListReverser:
    def __init__(self, input_list):
        self.list = input_list

    def reverse_in_place(self):
        left = 0
        right = len(self.list) - 1
        while left < right:
            self.list[left], self.list[right] = (self.list[right], self.list[left])
            left += 1
            right -= 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    reverser.reverse_in_place()
    print(reverser.list)