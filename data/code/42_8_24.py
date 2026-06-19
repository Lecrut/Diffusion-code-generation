def build_string(parts, separator=''):
    return separator.join(parts)
if __name__ == '__main__':
    parts = ['apple', 'banana', 'cherry']
    print(build_string(parts))
    print(build_string(parts, ' '))
    print(build_string(parts, ','))