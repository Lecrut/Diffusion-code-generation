def count_consonants(text):
    import unicodedata
    
    vowels = set('aeiouAEIOU')
    consonants = set()
    
    for char in text:
        if unicodedata.category(char).startswith('L'):
            consonants.add(char.lower())
            
    consonants -= vowels
    
    return len(consonants)

if __name__ == '__main__':
    sample_text = "Hello, World! 你好 世界 🌍"
    result = count_consonants(sample_text)
    print(result)