import sys
def remove_spaces(input_string):
    return input_string.replace(" ", "")
if __name__ == '__main__':
    test_string = "This is a sample string with spaces"
    result = remove_spaces(test_string)
    print(result)