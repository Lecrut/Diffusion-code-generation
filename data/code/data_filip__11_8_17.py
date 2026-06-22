def find_characters_appearing_twice(input_string: str) -> list:
    char_counts = {}
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    result = [char for char, count in char_counts.items() if count == 2]
    result.sort()
    
    return result

if __name__ == '__main__':
    sample_string = "aabbccddeeffgghhiijjkkllmmnnooppqqrsttuuvvwwxxyyzz"
    output = find_characters_appearing_twice(sample_string)
    print(output)