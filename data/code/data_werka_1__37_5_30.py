def combine_strings(str1, str2):
    return str1 + str2

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello, ",
        "farewell": "Goodbye, "
    }
    result1 = combine_strings(sample_values["greeting"], "World!")
    result2 = combine_strings(sample_values["farewell"], "Universe!")
    print(result1)
    print(result2)