def join_strings(str1, str2):
    return f"{str1} {str2}"

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello",
        "farewell": "Goodbye"
    }
    result = join_strings(sample_values["greeting"], sample_values["farewell"])
    print(result)