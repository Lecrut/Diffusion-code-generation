def count_special_chars(s):
    special_chars = set('!@#$%^&*()_+-=[]{}|;:,.<>?/~`')
    count = 0
    has_special = False
    for char in s:
        if char in special_chars:
            count += 1
            has_special = True
    return count, has_special

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "No special characters here",
        "Special chars: @#$%",
        "Another one with ! and ?"
    ]
    for s in sample_strings:
        result = count_special_chars(s)
        print(result)