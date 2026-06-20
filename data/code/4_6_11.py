def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == "__main__":
    sample_string = "Héllo Wörld! 123 Café"
    result = count_consonants(sample_string)
    print(result)