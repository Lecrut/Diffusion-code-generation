def count_vowels(text):
    translation_table = str.maketrans("aeiouAEIOU", "1111111111")
    translated = text.translate(translation_table)
    count = 0
    for char in translated:
        if char == "1":
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Programming is fun and powerful for everyone who wants to explore"
    result = count_vowels(sample_string)
    print(result)