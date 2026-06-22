def join_with_delimiter(list_of_strings, delimiter):
    return ''.join([element + delimiter for element in list_of_strings])[:-len(delimiter)]

if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "date"]
    separator = "; "
    output = join_with_delimiter(fruits, separator)
    print(output)