def check_equality(item1, item2):
    return item1 is item2 or (isinstance(item1, type(item2)) and item1 == item2)
if __name__ == '__main__':
    sample1 = [1, 2, 3]
    sample2 = [1, 2, 3]
    sample3 = sample1
    print(check_equality(sample1, sample2))
    print(check_equality(sample1, sample3))
    print(check_equality(42, 42))
    print(check_equality('hello', 'hello'))
    print(check_equality('hello', 'world'))