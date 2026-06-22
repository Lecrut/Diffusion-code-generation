def find_chars_appearing_twice(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    result = [char for char, count in char_counts.items() if count == 2]
    result.sort()
    return result

if __name__ == '__main__':
    sample_string = "programming"
    print(find_chars_appearing_twice(sample_string))