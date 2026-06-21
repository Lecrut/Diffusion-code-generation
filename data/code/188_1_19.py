class ListReverser:
    def __init__(self, input_list):
        self.input_list = input_list

    def reverse_in_place(self):
        left = 0
        right = len(self.input_list) - 1
        while left < right:
            self.input_list[left], self.input_list[right] = self.input_list[right], self.input_list[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    reverser = ListReverser([1, 2, 3, 4, 5])
    print("Original list:", reverser.input_list)
    reverser.reverse_in_place()
    print("Reversed in-place:", reverser.input_list)