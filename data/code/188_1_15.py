class InPlaceReverser:
    @staticmethod
    def reverse_in_place(lst):
        left = 0
        right = len(lst) - 1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    InPlaceReverser.reverse_in_place(sample_list)
    print(sample_list)