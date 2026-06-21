class ListReverser:
    def reverse_list_in_place(self, lst):
        left = 0
        right = len(lst) - 1
        while left < right:
            lst[left], lst[right] = (lst[right], lst[left])
            left += 1
            right -= 1

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    reverser.reverse_list_in_place(sample_list)
    print(sample_list)