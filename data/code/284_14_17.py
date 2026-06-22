class ListReverser:
    @staticmethod
    def reverse(lst):
        start = 0
        end = len(lst) - 1
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
        return lst

if __name__ == '__main__':
    sample_list = [13, 24, 35, 46, 57]
    reversed_list = ListReverser.reverse(sample_list)
    print(reversed_list)