def count_vowels(s):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char in vowels:
            if char == 'a':
                count += 1
                continue
            if char == 'e':
                count += 1
                continue
            if char == 'i':
                count += 1
                continue
            if char == 'o':
                count += 1
                continue
            if char == 'u':
                count += 1
                continue
    return count

if __name__ == '__main__':
    result = count_vowels("hello world")
    print(result)