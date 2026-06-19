def join_strings_efficiently(string_list):
    if not isinstance(string_list, list):
        raise TypeError("Input must be a list")
    for item in string_list:
        if not isinstance(item, str):
            raise ValueError("All items in the list must be strings")
    return "".join(string_list)

class StringJoiner:
    def __init__(self, string_list):
        self.string_list = string_list

    def join(self):
        return join_strings_efficiently(self.string_list)

if __name__ == '__main__':
    try:
        list1 = ["hello", "world", "python"]
        joiner1 = StringJoiner(list1)
        print(joiner1.join())

        list2 = ["a", "b", "c", "d", "e"]
        joiner2 = StringJoiner(list2)
        print(joiner2.join())

        list3 = ["one", "two", "three", "four"]
        joiner3 = StringJoiner(list3)
        print(joiner3.join())
    except (TypeError, ValueError) as e:
        print(e)