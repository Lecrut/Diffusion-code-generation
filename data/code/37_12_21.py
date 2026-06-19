def combine_strings(str1, str2):
    return ''.join((str1, str2))

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello, ",
        "subject": "World!"
    }
    result = combine_strings(sample_values["greeting"], sample_values["subject"])
    print(result)