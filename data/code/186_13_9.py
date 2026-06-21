class ListReverser:
    @staticmethod
    def reverse(lst):
        left, right = 0, len(lst) - 1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    sample_list = [5, 4, 3, 2, 1]
    ListReverser.reverse(sample_list)
    print(sample_list)