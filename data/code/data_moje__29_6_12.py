def count_vowels(s):
    count = 0
    vowels = set('aeiouAEIOU')
    for char in s:
        if char in vowels:
            count += 1
            if char == 'a':
                break
    return count

if __name__ == '__main__':
    text = "apple"
    result = count_vowels(text)
    print(result)