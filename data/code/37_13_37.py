def merge_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    
    first_part = str1[:len(str1)//2]
    second_part = str1[len(str1)//2:]
    merged_result = first_part + str2 + second_part
    
    return merged_result

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    result = merge_strings(string_a, string_b)
    print(result)

    another_string_a = "Python"
    another_string_b = "Programming"
    another_result = merge_strings(another_string_a, another_string_b)
    print(another_result)