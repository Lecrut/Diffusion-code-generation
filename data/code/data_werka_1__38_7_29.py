def find_unique_letters_at_least_twice(s):
    letter_count = {}
    for char in s.lower():
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    
    result = [letter for letter, count in letter_count.items() if count >= 2]
    return result

if __name__ == '__main__':
    sample_string = "This is a simple test string."
    print(find_unique_letters_at_least_twice(sample_string))