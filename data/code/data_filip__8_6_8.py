def split_and_strip(s):
    return [part.strip() for part in s.split(',') if part.strip()]

if __name__ == '__main__':
    sample_string = "apple,  banana ,  , cherry,  , date  , , "
    result = split_and_strip(sample_string)
    print(result)