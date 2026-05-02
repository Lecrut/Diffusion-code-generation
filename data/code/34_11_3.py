import re
def capitalize_first_letter_only(text):
    return " ".join(word.capitalize() for word in text.split())
if __name__ == '__main__':
    sample1 = "hello world this is a test"
    sample2 = "tHis Is A TeSt"
    sample3 = "a short example"
    sample4 = "singleword"
    sample5 = ""
    sample6 = "  leading and trailing spaces  "
    print(f"'{sample1}' -> '{capitalize_first_letter_only(sample1)}'")
    print(f"'{sample2}' -> '{capitalize_first_letter_only(sample2)}'")
    print(f"'{sample3}' -> '{capitalize_first_letter_only(sample3)}'")
    print(f"'{sample4}' -> '{capitalize_first_letter_only(sample4)}'")
    print(f"'{sample5}' -> '{capitalize_first_letter_only(sample5)}'")
    print(f"'{sample6}' -> '{capitalize_first_letter_only(sample6)}'")