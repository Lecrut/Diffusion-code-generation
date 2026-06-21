VOWELS = set('aeiouAEIOU')

def count_vowels(s):
    return sum(1 for char in s if char in VOWELS)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud is a great place to work!"
    print(count_vowels(sample_string))