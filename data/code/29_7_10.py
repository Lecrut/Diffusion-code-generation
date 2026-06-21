def count_vowels(s):
    total = 0
    for char in s:
        if char in "aeiouAEIOU":
            total += 1
    return total

if __name__ == '__main__':
    text = "Hello World"
    result = count_vowels(text)
    print(result)