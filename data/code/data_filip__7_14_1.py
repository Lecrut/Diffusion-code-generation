SPECIAL_CHARACTERS = set("!@#$%^&*()_+-=[]{}|;':\",./<>?`~")

def has_special_characters(s):
    return bool(set(s).intersection(SPECIAL_CHARACTERS))

if __name__ == '__main__':
    sample_string = "hello world!"
    print(has_special_characters(sample_string))