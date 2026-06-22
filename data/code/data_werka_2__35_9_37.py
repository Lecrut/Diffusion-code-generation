def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud is an innovative technology company."
    print(count_vowels(sample_string))