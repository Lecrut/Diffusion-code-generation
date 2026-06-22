def get_first_word(text):
    words = text.split()
    if words:
        return words[0]
    else:
        return ""

if __name__ == '__main__':
    sample1 = "Hello world"
    sample2 = "   leading spaces and multiple words"
    sample3 = "singleword"
    sample4 = ""
    
    print(f"Input: '{sample1}', Output: '{get_first_word(sample1)}'")
    print(f"Input: '{sample2}', Output: '{get_first_word(sample2)}'")
    print(f"Input: '{sample3}', Output: '{get_first_word(sample3)}'")
    print(f"Input: '{sample4}', Output: '{get_first_word(sample4)}'")