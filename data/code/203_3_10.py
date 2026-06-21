LEXICOGRAPHICAL_COMPARE_CONSTANTS = {
    "LESS_THAN": -1,
    "EQUAL_TO": 0,
    "GREATER_THAN": 1
}

def compare_strings(str1, str2):
    if str1 < str2:
        return LEXICOGRAPHICAL_COMPARE_CONSTANTS["LESS_THAN"]
    elif str1 > str2:
        return LEXICOGRAPHICAL_COMPARE_CONSTANTS["GREATER_THAN"]
    else:
        return LEXICOGRAPHICAL_COMPARE_CONSTANTS["EQUAL_TO"]

if __name__ == '__main__':
    sample_str1 = "zebra"
    sample_str2 = "apple"
    result = compare_strings(sample_str1, sample_str2)
    print(result)