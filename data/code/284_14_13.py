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
    sample_list = [2, 4, 6, 8, 10]
    reversed_list = ListReverser.reverse(sample_list)
    print(reversed_list)