def first_letter(s):
    return s[0] if s else ''
if __name__ == '__main__':
    print(first_letter('Hello'))
    print(first_letter(''))
    print(first_letter('World'))