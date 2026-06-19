def find_repeated_letters(s):
    letter_count = {}
    for char in s:
        if char.isalpha():
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    
    repeated_letters = {char for char, count in letter_count.items() if count > 1}
    return repeated_letters

if __name__ == '__main__':
    sample_string = "Programming is fun!"
    result = find_repeated_letters(sample_string)
    print(result)