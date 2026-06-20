def split_and_trim(string):
    return [part.strip() for part in string.split(',') if part.strip()]

if __name__ == '__main__':
    result = split_and_trim('  hello , world ,  ,  foo  ')
    print(result)