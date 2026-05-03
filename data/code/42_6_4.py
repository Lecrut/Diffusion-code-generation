import itertools
def join_strings_efficient(list_of_strings):
    return "".join(list_of_strings)
if __name__ == '__main__':
    data = ["hello", "world", "python", "efficient"]
    result = join_strings_efficient(data)
    print(result)