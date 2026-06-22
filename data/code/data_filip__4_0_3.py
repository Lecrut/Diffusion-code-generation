def count_consonants(text: str) -> int:
    consonants = set('bcdfghjklmnpqrstvwxyz')
    return sum(1 for char in text if char.lower() in consonants)

if __name__ == '__main__':
    sample_values = [
        "Hello World!",
        "Python Programming",
        "AEIOU",
        "12345!@#$%",
        "",
        "bcdfghjklmnpqrstvwxyz"
    ]
    for sample in sample_values:
        print(count_consonants(sample))