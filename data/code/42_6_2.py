import itertools
def join_strings_efficiently(list_of_strings):
    return "".join(list_of_strings)
if __name__ == '__main__':
    data = ["hello", " ", "world", "!"]
    result = join_strings_efficiently(data)
    print(result)