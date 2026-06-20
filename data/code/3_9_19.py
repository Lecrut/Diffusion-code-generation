def remove_vowels(text):
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans("", "", vowels)
    return text.translate(trans_table)

if __name__ == "__main__":
    sample_string = "Hello World"
    result = remove_vowels(sample_string)
    print(result)