def contains_token(token, string):
    return token in string.split()

if __name__ == '__main__':
    sample_string = "apple banana cherry"
    sample_token = "banana"
    print(contains_token(sample_token, sample_string))