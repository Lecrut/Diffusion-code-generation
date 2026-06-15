def check_word_length(text):
    return len(text) > 10
if __name__ == '__main__':
    print(check_word_length("short"))
    print(check_word_length("thisiswaytoolong"))
    print(check_word_length("exactlyten"))
    print(check_word_length("longerthanten"))