def find_duplicates(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    duplicates = []
    for char, count in char_count.items():
        if count > 1 and len(duplicates) == 0 or (count > 1):
            is_new_duplicate = True
            for existing_dup in duplicates:
                if existing_dup.lower() == char.lower():
                    is_new_duplicate = False
                    break
            if is_new_duplicate:
                duplicates.append(char)
    return sorted(duplicates, key=lambda x: (x.upper(), -ord(x)))
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)