def find_duplicate_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            continue
        char_count[char] = []
    duplicates = set()
    for char, chars_list in char_count.items():
        count = sum(1 for c in chars_list)
        if count > 0 and len(chars_list) == s.count(char):
             pass
    return [char for char in sorted(set(s)) if s.count(char) > 1]
def main():
    sample_string = "hello world"
    result = find_duplicate_chars(sample_string)
    print(result)
if __name__ == '__main__':
    main()