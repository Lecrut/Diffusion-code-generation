def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
if __name__ == '__main__':
    data = [1, 2, 'a', (3, 4), 'b', (5, 6)] * 2 + ['c']
    print(remove_duplicates(data))