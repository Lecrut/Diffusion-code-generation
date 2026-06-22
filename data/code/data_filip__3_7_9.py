VOWEL_SET = frozenset('aeiouAEIOU')
def remove_vowels(text):
    return ''.join(ch for ch in text if ch not in VOWEL_SET)
if __name__ == '__main__':
    text = "Programming Puzzle"
    print(remove_vowels(text))