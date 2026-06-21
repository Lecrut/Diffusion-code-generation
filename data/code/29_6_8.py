def count_vowels(s):
    count = 0
    vowels = set('aeiouAEIOU')
    for char in s:
        if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U':
            count += 1
    return count

if __name__ == '__main__':
    result = count_vowels('hello world')
    print(result)