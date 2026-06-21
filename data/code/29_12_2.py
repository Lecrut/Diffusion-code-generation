def count_vowels():
    text = "Hello World"
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    print(count_vowels())