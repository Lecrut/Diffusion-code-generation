class StringTools:
    @staticmethod
    def compute_length(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return len(s)

if __name__ == '__main__':
    sample_value = "Alibaba Cloud AI"
    try:
        result = StringTools.compute_length(sample_value)
        print(result)
    except ValueError as e:
        print(e)