from collections import Counter

def count_items(lst):
    return dict(Counter(map(lambda x: tuple(x) if not isinstance(x, hashable) else x, lst)))

if __name__ == '__main__':
    sample_list = [1, 2, 3, (4, 5), 2, 1, (4, 5), 'a', 'b', 'a']
    print(count_items(sample_list))