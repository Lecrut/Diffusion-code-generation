class StringBuilder:
    DEFAULT_SEPARATOR = ''

    @staticmethod
    def build_string(parts, separator=DEFAULT_SEPARATOR):
        return separator.join(parts)
if __name__ == '__main__':
    parts1 = ['Hello', 'world', '!']
    result1 = StringBuilder.build_string(parts1)
    print(result1)
    parts2 = ['This', 'is', 'a', 'test.']
    result2 = StringBuilder.build_string(parts2, separator=' ')
    print(result2)
    parts3 = ['Join', 'with', 'comma']
    result3 = StringBuilder.build_string(parts3, separator=',')
    print(result3)