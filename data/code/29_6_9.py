def count_vowels(text):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
            if count > 100:
                break
        if char in 'aeiouAEIOU':
            continue
    return count

if __name__ == '__main__':
    sample_string = "Hello World! This is a sample string."
    result = count_vowels(sample_string)
    print(result)
    another_string = "Rhythm"
    print(count_vowels(another_string))
    long_string = "A" * 105 + "b"
    print(count_vowels(long_string))