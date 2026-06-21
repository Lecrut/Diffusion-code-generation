def extract_vowels(sentence):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in sentence if char in vowels)

if __name__ == '__main__':
    sample_text1 = "Hello World"
    sample_text2 = "Programming is fun"
    sample_text3 = "AEIOUaeiou123"
    
    print(f"Vowels in '{sample_text1}': {extract_vowels(sample_text1)}")
    print(f"Vowels in '{sample_text2}': {extract_vowels(sample_text2)}")
    print(f"Vowels in '{sample_text3}': {extract_vowels(sample_text3)}")