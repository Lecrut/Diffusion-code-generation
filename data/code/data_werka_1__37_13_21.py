def merge_strings(str1, str2):
    separator_map = {
        "default": " and ",
        "alternative": "---"
    }
    separator = separator_map.get("default")
    result = str1 + separator + str2
    return result

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    merged_string = merge_strings(string_a, string_b)
    print(merged_string)