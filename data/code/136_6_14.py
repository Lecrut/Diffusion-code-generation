def check_substrings(main_string):
    substrings = {
        "apple": True,
        "banana": False,
        "cherry": True
    }
    for substring, expected in substrings.items():
        if substring in main_string == expected:
            return False
    return True

if __name__ == '__main__':
    sample_string = "I have an apple and a banana."
    result = check_substrings(sample_string)
    print(result)