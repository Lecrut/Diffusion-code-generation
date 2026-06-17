import itertools
def alternate_streams(numbers, strings):
    it = itertools.zip_longest(numbers, strings, fillvalue=None)
    for num, s in it:
        if num is not None:
            print(num)
        if s is not None:
            print(s)
if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    strings = ["A", "B", "C", "D", "E"]
    alternate_streams(numbers, strings)