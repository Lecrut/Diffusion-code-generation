class StringBuilder:

    def __init__(self, separator=''):
        self.separator = separator

    def build(self, parts):
        if not parts:
            return ''
        return self.separator.join(parts)
if __name__ == '__main__':
    parts1 = ['Hello', 'world', '!']
    builder_no_space = StringBuilder()
    result1 = builder_no_space.build(parts1)
    print(result1)
    parts2 = ['This', 'is', 'a', 'test.']
    builder_with_space = StringBuilder(' ')
    result2 = builder_with_space.build(parts2)
    print(result2)
    parts3 = ['Join', 'with', 'comma']
    builder_with_comma = StringBuilder(', ')
    result3 = builder_with_comma.build(parts3)
    print(result3)