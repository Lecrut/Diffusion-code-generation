def contains_token(string, token):
    return token in string.split()

if __name__ == '__main__':
    sample_string = "apple banana cherry"
    sample_token = "banana"
    print(contains_token(sample_string, sample_token))