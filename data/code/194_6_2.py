def find_longest_string(iterable):
    if not iterable:
        return None
    longest_string = ""
    for s in iterable:
        if len(s) > len(longest_string):
            longest_string = s
    yield longest_string
if __name__ == '__main__':
    data = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result_generator = find_longest_string(data)
    longest = None
    for item in result_generator:
        longest = item
        break
    print(longest)
    data2 = ["short", "longer", "longest_one", "medium"]
    result_generator2 = find_longest_string(data2)
    longest2 = None
    for item in result_generator2:
        longest2 = item
        break
    print(longest2)
    data3 = []
    result_generator3 = find_longest_string(data3)
    longest3 = None
    for item in result_generator3:
        longest3 = item
        break
    print(longest3)