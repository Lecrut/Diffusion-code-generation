def combine_strings(str1, str2):
    return f"{str1}{str2}"

if __name__ == '__main__':
    first_part = "OpenAI"
    second_part = "ChatGPT"
    full_string = combine_strings(first_part, second_part)
    print(full_string)
    
    another_first = "Python"
    another_second = "Programming"
    combined_result = combine_strings(another_first, another_second)
    print(combined_result)