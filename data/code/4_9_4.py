CONSONANTS = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def count_consonants(text):
    return sum(1 for char in text if char in CONSONANTS)

if __name__ == '__main__':
    sample_text = "Hello World! 123"
    print(count_consonants(sample_text))