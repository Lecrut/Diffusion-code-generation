CHARACTER_COUNT = {}

def count_characters(s):
    for char in s:
        if char in CHARACTER_COUNT:
            CHARACTER_COUNT[char] += 1
        else:
            CHARACTER_COUNT[char] = 1

def first_non_repeating_char(s):
    count_characters(s)
    for char in s:
        if CHARACTER_COUNT[char] == 1:
            return char
    return None

if __name__ == '__main__':
    print(first_non_repeating_char("swiss"))