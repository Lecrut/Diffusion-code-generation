vowels = "aeiouAEIOU"

def count_vowels(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(count_vowels(sample_string))