def count_vowels(text):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    test_string = "Hello World!"
    result = count_vowels(test_string)
    print(result)