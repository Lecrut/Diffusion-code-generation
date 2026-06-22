def transform_string(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    result = transform_string("hello world")
    print(result)