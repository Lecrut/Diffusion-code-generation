def count_vowels(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    samples = ["Hello World", "", "Python", "AEIOUaeiou", "12345!@#$%"]
    for sample in samples:
        result = count_vowels(sample)
        print(result)