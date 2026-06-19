class StringProcessor:
    @staticmethod
    def remove_spaces(s):
        return ''.join(s.split())

if __name__ == '__main__':
    sample_string = "  This is a sample string with   various spaces. \nIt has   multiple lines. "
    result = StringProcessor.remove_spaces(sample_string)
    print(result)