def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
if __name__ == '__main__':
    data = [1, 2, 3, 'a', 'b', 4, 'c', 5]
    print(remove_duplicates(data))