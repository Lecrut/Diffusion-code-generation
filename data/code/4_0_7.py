def count_consonants(s: str) -> int:
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == "__main__":
    print(count_consonants("Hello, World!"))
    print(count_consonants("Python3.9"))
    print(count_consonants("AEIOU"))
    print(count_consonants("bcdfg"))
    print(count_consonants(""))
    print(count_consonants("12345!@#"))