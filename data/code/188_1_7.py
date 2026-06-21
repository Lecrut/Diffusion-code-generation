class ListReverser:
    def reverse_in_place(self, lst):
        left = 0
        right = len(lst) - 1
        while left < right:
            lst[left], lst[right] = (lst[right], lst[left])
            left += 1
            right -= 1

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    print(f"Original list: {sample_list}")
    reverser.reverse_in_place(sample_list)
    print(f"Reversed in-place list: {sample_list}")