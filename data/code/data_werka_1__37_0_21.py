def combine_strings(str1, str2):
    return str1 + str2

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello",
        "farewell": "World"
    }
    
    result = combine_strings(sample_values["greeting"], sample_values["farewell"])
    print(result)