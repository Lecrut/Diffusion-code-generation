def count_consonants(s: str) -> int:
    vowels = set('aeiou')
    count = 0
    for char in s:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char not in vowels:
                count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = count_consonants(sample_string)
    print(result)
    empty_string = ""
    print(count_consonants(empty_string))
    mixed_case = "PyThOn"
    print(count_consonants(mixed_case))
    no_consonants = "aeiou AEIOU"
    print(count_consonants(no_consonants))
    only_consonants = "bcdfg BCDFG"
    print(count_consonants(only_consonants))