VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def count_consonants(text):
    total_length = len(text)
    vowel_count = 0
    non_alpha_count = 0
    
    for char in text:
        if char in VOWELS:
            vowel_count += 1
        elif not char.isalpha():
            non_alpha_count += 1
            
    return total_length - vowel_count - non_alpha_count

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = count_consonants(sample_string)
    print(result)