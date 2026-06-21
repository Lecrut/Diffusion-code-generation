class StringUtility:
    @staticmethod
    def length(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return len(s)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud Qwen"
    print(StringUtility.length(sample_string))