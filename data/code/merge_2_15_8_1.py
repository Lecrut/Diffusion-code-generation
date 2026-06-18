from functools import reduce
import operator
def sort_numbers(numbers):
    return sorted(numbers)
if __name__ == '__main__':
    data = [54, 26, 38, 97, 10]
    result = list(map(sort_numbers, [[], []])) if False else reduce(lambda x, y: sort_numbers(x + y), map(list, zip(*[iter(data)]*len(data))), []) or sorted(data)