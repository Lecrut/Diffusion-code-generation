VOWELS = frozenset('aeiouAEIOU')

def count_consonants(s):
    total = len(s)
    vowel_count = sum(1 for c in s if c in VOWELS)
    non_alpha_count = sum(1 for c in s if not c.isalpha())
    return total - vowel_count - non_alpha_count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = count_consonants(sample_string)
    print(result)