def validate_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")

def calculate_length_difference(str1, str2):
    return len(str1) - len(str2)

def find_first_differing_index(str1, str2):
    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        if str1[i] != str2[i]:
            return i
    return None if len(str1) == len(str2) else -1

def compare_strings(str1, str2):
    validate_strings(str1, str2)
    length_diff = calculate_length_difference(str1, str2)
    first_diff_index = find_first_differing_index(str1, str2)
    return {'length_difference': length_diff, 'first_differing_index': first_diff_index}

if __name__ == '__main__':
    str1 = 'example'
    str2 = 'exemplary'
    result = compare_strings(str1, str2)
    print(result)