def join_with_delimiter(list_of_strings, delimiter):
    result = ""
    for i in range(len(list_of_strings)):
        result += list_of_strings[i]
        if i < len(list_of_strings) - 1:
            result += delimiter
    return result

if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "date"]
    separator = "; "
    output = join_with_delimiter(fruits, separator)
    print(output)