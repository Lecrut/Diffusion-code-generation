def count_vowels(s: str) -> int: return sum(1 for c in s.lower() if c in "aeiou")

if __name__ == '__main__': 
    print(count_vowels("Hello, World!"))  # Expected output: 2