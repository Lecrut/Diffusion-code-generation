def count_vowels(s: str) -> int:
    return sum(1 for c in s if c.lower() in "aeiou")

if __name__ == '__main__':
    sample_string = "Hello World"
    result = count_vowels(sample_string)
    print(result)