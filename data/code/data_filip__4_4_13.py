VOWELS = set('aeiouAEIOU')

def count_consonants(text):
    if not text:
        return 0
    
    vowel_count = 0
    non_alpha_count = 0
    
    for char in text:
        if char in VOWELS:
            vowel_count += 1
        elif not char.isalpha():
            non_alpha_count += 1
    
    return len(text) - vowel_count - non_alpha_count

if __name__ == '__main__':
    sample = "Python3.9 is fun!"
    print(count_consonants(sample))