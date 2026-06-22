def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    return sum(1 for char in s if char.lower() in consonants)

if __name__ == '__main__':
    sample_string = "Hello World!"
    result = count_consonants(sample_string)
    print(result)