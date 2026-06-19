def combine_strings(str1, str2):
    return str1 + str2

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello, ",
        "farewell": "Goodbye!"
    }
    result = combine_strings(sample_values["greeting"], "World!")
    print(result)