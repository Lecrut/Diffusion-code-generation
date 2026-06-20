def has_special_characters(input_string):
    ascii_printable_ranges = (
        list(range(32, 127))
    )
    alphanumerics = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    spaces_and_common = set(" \t\n\r")
    for char in input_string:
        if char in alphanumerics:
            continue
        if char in spaces_and_common:
            continue
        if ord(char) in ascii_printable_ranges:
            return True
    return False

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Hello@World!"
    sample3 = "12345"
    print(has_special_characters(sample1))
    print(has_special_characters(sample2))
    print(has_special_characters(sample3))