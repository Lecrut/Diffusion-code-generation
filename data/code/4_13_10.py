def count_consonants(s):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    return sum(1 for char in s if char in consonants)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_consonants(sample_text)
    print(result)