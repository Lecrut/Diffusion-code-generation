def are_equal(item1, item2):
    return item1 == item2
if __name__ == '__main__':
    print(are_equal(5, 5))
    print(are_equal('hello', 'world'))
    print(are_equal([1, 2, 3], [1, 2, 3]))
    print(are_equal([1, 2, 3], [3, 2, 1]))