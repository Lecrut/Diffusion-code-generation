def find_duplicates(s):
    char_count = {}
    result_list = []
    for char in s:
        if char in char_count and not (char in [c for c in result_list]):
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            found_char = False
            for item in result_list:
                if item == char:
                    found_char = True
                    break
            if not found_char:
                result_list.append(char)
    return sorted(result_list, key=lambda x: s.find(x))
def main():
    sample_string = "hello world"
    duplicates = find_duplicates(sample_string)
    print(duplicates)
if __name__ == '__main__':
    main()