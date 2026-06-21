def check_for_word(unicode_string, target_word):
    normalized_string = unicode_string.encode('utf-8').decode('utf-8', errors='ignore')
    return target_word in normalized_string

if __name__ == '__main__':
    sample_string_1 = "This is a normal line. Another line with critical information. Final line."
    sample_string_2 = "No critical words here.\nJust some text."
    sample_string_3 = "critical is the key\nanother line"
    sample_string_4 = "Line with écritical and some bad encoding \xff"

    print(f"Sample 1 result: {check_for_word(sample_string_1, 'critical')}")
    print(f"Sample 2 result: {check_for_word(sample_string_2, 'critical')}")
    print(f"Sample 3 result: {check_for_word(sample_string_3, 'critical')}")
    print(f"Sample 4 result: {check_for_word(sample_string_4, 'critical')}")