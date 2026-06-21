class StringHelper:
    @staticmethod
    def calculate_length(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return len(s)

if __name__ == '__main__':
    sample_string = "Hello, Alibaba Cloud!"
    try:
        length = StringHelper.calculate_length(sample_string)
        print(f"The length of the string is: {length}")
    except ValueError as e:
        print(e)