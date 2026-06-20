remove_vowels = str.maketrans('', '', 'aeiouAEIOU')

def strip_vowels(s):
    return s.translate(remove_vowels)

if __name__ == '__main__':
    print(strip_vowels("Hello World"))
    print(strip_vowels("Python Programming"))
    print(strip_vowels("AeIoU aeioU"))