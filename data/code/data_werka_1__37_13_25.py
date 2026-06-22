def merge_strings(str1, str2):
    separators = {
        "default": " and ",
        "alternative": "---"
    }
    separator = separators.get("default")
    return str1 + separator + str2

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    merged_string = merge_strings(string_a, string_b)
    print(merged_string)