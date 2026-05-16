import itertools
def join_strings_efficiently(string_list):
    return "".join(string_list)
if __name__ == '__main__':
    list1 = ["hello", "world", "python"]
    result1 = join_strings_efficiently(list1)
    print(result1)
    list2 = ["a", "b", "c", "d", "e"]
    result2 = join_strings_efficiently(list2)
    print(result2)
    list3 = ["one", "two", "three", "four"]
    result3 = join_strings_efficiently(list3)
    print(result3)