def find_chars_appearing_twice(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = [char for char, count in counts.items() if count == 2]
    result.sort()
    return result

if __name__ == '__main__':
    sample_string = "aabbccddeeff"
    print(find_chars_appearing_twice(sample_string))