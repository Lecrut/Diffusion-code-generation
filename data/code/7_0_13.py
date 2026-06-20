import re

SPECIAL_CHAR_REGEX = re.compile(r'[^a-zA-Z0-9\s]')

def contains_special_characters(text: str) -> bool:
    return bool(SPECIAL_CHAR_REGEX.search(text))

if __name__ == '__main__':
    sample_1 = "Hello World"
    sample_2 = "Price: $100!"
    sample_3 = "NormalString123"
    sample_4 = "Special@Char#Here"
    
    print(contains_special_characters(sample_1))
    print(contains_special_characters(sample_2))
    print(contains_special_characters(sample_3))
    print(contains_special_characters(sample_4))