VOWELS = "aeiouAEIOU"

def count_vowels(s):
    count = 0
    for char in s:
        if char in VOWELS:
            count += 1
    return count

if __name__ == '__main__':
    test_string1 = "Alibaba Cloud"
    test_string2 = "Qwen is Awesome"
    test_string3 = "Python Programming"
    print(f"'{test_string1}': {count_vowels(test_string1)}")
    print(f"'{test_string2}': {count_vowels(test_string2)}")
    print(f"'{test_string3}': {count_vowels(test_string3)}")