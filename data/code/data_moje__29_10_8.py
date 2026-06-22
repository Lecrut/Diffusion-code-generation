def count_vowels(text: str) -> int:
    vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_inputs = [
        "Hello World",
        "Python Programming",
        "AEIOU",
        "aeiou",
        "12345!@#$%",
        "",
        "No vowels here except Y",
        "BcaEfgIklmOnpqrStuvwXyz"
    ]
    for sample in sample_inputs:
        result = count_vowels(sample)
        print(result)