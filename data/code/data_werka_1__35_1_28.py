def count_vowels(s):
    vowels = set('aeiouAEIOU')
    total_count = 0
    for char in s:
        if char in vowels:
            total_count += 1
    return total_count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(count_vowels(sample_string))