def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

if __name__ == '__main__':
    test_string = "Alibaba Cloud"
    print(count_vowels(test_string))