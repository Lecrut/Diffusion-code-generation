class StringJoiner:
    def __init__(self, strings):
        self.strings = strings

    def join(self):
        return "".join(self.strings)

if __name__ == '__main__':
    list1 = ["hello", "world", "python"]
    joiner1 = StringJoiner(list1)
    result1 = joiner1.join()
    print(result1)

    list2 = ["a", "b", "c", "d", "e"]
    joiner2 = StringJoiner(list2)
    result2 = joiner2.join()
    print(result2)

    list3 = ["one", "two", "three", "four"]
    joiner3 = StringJoiner(list3)
    result3 = joiner3.join()
    print(result3)