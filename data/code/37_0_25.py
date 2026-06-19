def combine_strings(str1, str2):
    return str1 + str2

if __name__ == '__main__':
    strings = {
        'greeting': "Hello",
        'farewell': "World"
    }
    result = combine_strings(strings['greeting'], strings['farewell'])
    print(result)