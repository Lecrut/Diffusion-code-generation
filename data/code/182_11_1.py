import string
def separate_string_into_list_of_characters(input_string):
    return list(input_string)
if __name__ == '__main__':
    sample_string = "Hello World"
    result = separate_string_into_list_of_characters(sample_string)
    print(result)