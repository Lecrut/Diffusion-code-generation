def combine_strings(str1, str2):
    return f"{str1} {str2}"

if __name__ == '__main__':
    sample_values = {
        "string_a": "hello",
        "string_b": "world"
    }
    
    result = combine_strings(sample_values["string_a"], sample_values["string_b"])
    print(result)