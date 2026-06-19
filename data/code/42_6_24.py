class StringJoiner:
    SEPARATOR = ""

    @staticmethod
    def join_strings(string_list):
        return "".join(string_list)

if __name__ == '__main__':
    list1 = ["hello", "world", "python"]
    result1 = StringJoiner.join_strings(list1)
    print(result1)
    
    list2 = ["a", "b", "c", "d", "e"]
    result2 = StringJoiner.join_strings(list2)
    print(result2)
    
    list3 = ["one", "two", "three", "four"]
    result3 = StringJoiner.join_strings(list3)
    print(result3)