def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "Python Programming", "AeIoU"]
    for string in sample_strings:
        print(f"Number of vowels in '{string}': {count_vowels(string)}")