second_to_last = lambda lst: lst[-2] if len(lst) >= 2 else (_ for _ in ()).throw(IndexError("List must have at least two items"))
if __name__ == '__main__':
    test_data = [5, 10, 15, 20, 25]
    print(second_to_last(test_data))