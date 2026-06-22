def build_string(parts, separator=''):
    return separator.join(parts)
if __name__ == '__main__':
    parts = ['Hello', 'world', 'this', 'is', 'a', 'test']
    print(build_string(parts))
    print(build_string(parts, ' '))
    print(build_string(parts, ','))