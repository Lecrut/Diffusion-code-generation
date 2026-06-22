UPPERCASE_CONST = 'upper'

def uppercase_strings(string_list):
    return [s.__getattribute__(UPPERCASE_CONST)() for s in string_list]

if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "script"]
    result = uppercase_strings(sample_list)
    for upper_string in result:
        print(upper_string)