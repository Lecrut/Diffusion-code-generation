def find_unique_letters_appearing_twice(s):
    letter_count = {}
    for char in s.lower():
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    return [letter for letter, count in letter_count.items() if count >= 2]

if __name__ == '__main__':
    sample_string = "aAabcBcCdeE"
    result = find_unique_letters_appearing_twice(sample_string)
    print(result)