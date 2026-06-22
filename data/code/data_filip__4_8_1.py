import string

def count_consonants(text):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == "__main__":
    sample_input = "Hello, World! 123"
    result = count_consonants(sample_input)
    print(result)