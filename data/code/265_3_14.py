def separate_by_ascii_value(phrase):
    even_chars = ''.join(char for char in phrase if ord(char) % 2 == 0)
    odd_chars = ''.join(char for char in phrase if ord(char) % 2 != 0)
    return even_chars, odd_chars

if __name__ == '__main__':
    sample_phrase1 = "Hello, World!"
    even1, odd1 = separate_by_ascii_value(sample_phrase1)
    print(even1)
    print(odd1)
    
    sample_phrase2 = "Python3.8"
    even2, odd2 = separate_by_ascii_value(sample_phrase2)
    print(even2)
    print(odd2)