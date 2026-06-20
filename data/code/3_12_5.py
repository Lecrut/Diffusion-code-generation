def remove_vowels(s):
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans("", "", vowels)
    return s.translate(trans_table)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)