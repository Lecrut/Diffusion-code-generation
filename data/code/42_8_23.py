class StringJoiner:

    def __init__(self, separator=''):
        self.separator = separator

    def join(self, parts):
        return self.separator.join(parts)
if __name__ == '__main__':
    parts1 = ['Hello', 'world', '!']
    parts2 = ['This', 'is', 'a', 'test.']
    joiner_no_space = StringJoiner()
    joiner_with_space = StringJoiner(' ')
    joiner_with_comma = StringJoiner(',')
    result1 = joiner_no_space.join(parts1)
    result2 = joiner_with_space.join(parts1)
    result3 = joiner_with_comma.join(parts2)
    print(result1)
    print(result2)
    print(result3)