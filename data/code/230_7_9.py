class StringToUpper:
    @staticmethod
    def to_upper_case(strings):
        return list(map(lambda s: s.upper() if isinstance(s, str) else None, strings))

if __name__ == '__main__':
    sample_list = ['hello', 'world', 123, 'python']
    uppercased_list = StringToUpper.to_upper_case(sample_list)
    print(uppercased_list)