from itertools import groupby
data = [('a', 1), ('b', 2), ('a', 3), ('c', 4), ('b', 5)]
key_func = lambda x: x[0]
grouped_data = [list(g) for k, g in groupby(sorted(data), key=key_func)]
if __name__ == '__main__':
    print(grouped_data)