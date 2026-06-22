from itertools import chain

class ListRepeater:
    @staticmethod
    def repeat_list(original, n):
        return list(chain.from_iterable([original] * n))

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    times = 3
    result = ListRepeater.repeat_list(sample_list, times)
    print(result)