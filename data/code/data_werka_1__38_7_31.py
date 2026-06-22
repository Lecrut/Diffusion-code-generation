def find_unique_letters_at_least_twice(s):
    s = s.lower()
    letter_count = {}
    for char in s:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    
    result = [letter for letter, count in letter_count.items() if count >= 2]
    return result

if __name__ == '__main__':
    sample_string = "Hello, World! This is a simple test."
    print(find_unique_letters_at_least_twice(sample_string))