def combine_strings(str1, str2):
    return f"{str1}{str2}"

if __name__ == '__main__':
    first_string = "Good morning, "
    second_string = "Earth!"
    combined_result = combine_strings(first_string, second_string)
    print(combined_result)

    another_first_string = "Let's code in "
    another_second_string = "Python."
    another_combined_result = combine_strings(another_first_string, another_second_string)
    print(another_combined_result)