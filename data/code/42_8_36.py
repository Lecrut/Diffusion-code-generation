def build_string(parts, separator=''):
    return separator.join(parts)
if __name__ == '__main__':
    parts1 = ['Hello', 'world']
    separator1 = ' '
    result1 = build_string(parts1, separator1)
    print(result1)
    parts2 = ['apple', 'banana', 'cherry']
    separator2 = ','
    result2 = build_string(parts2, separator2)
    print(result2)
    parts3 = ['one', 'two', 'three']
    separator3 = ''
    result3 = build_string(parts3, separator3)
    print(result3)