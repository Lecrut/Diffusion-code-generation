import re

def count_consonants(word):
    consonants = re.findall(r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]', word)
    return len(consonants)

if __name__ == '__main__':
    sample_word = "Hello, World! 123 @#%"
    result = count_consonants(sample_word)
    print(result)