def combine_strings(str1, str2):
    return f"{str1}{str2}"

if __name__ == '__main__':
    first_part = "Good morning, "
    second_part = "everyone!"
    combined_greeting = combine_strings(first_part, second_part)
    print(combined_greeting)

    first_programming_language = "Java"
    second_programming_language = "Script"
    full_language_name = combine_strings(first_programming_language, second_programming_language)
    print(full_language_name)