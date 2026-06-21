class StringUtilities:
    def __init__(self, s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        self.s = s

    @staticmethod
    def length(s):
        return len(s)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    print(StringUtilities.length(sample_string))