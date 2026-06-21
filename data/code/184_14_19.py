def contains_token(input_string, token):
    return token in input_string.split()

if __name__ == '__main__':
    sample_string = "apple banana cherry"
    token_to_check = "banana"
    print(contains_token(sample_string, token_to_check))