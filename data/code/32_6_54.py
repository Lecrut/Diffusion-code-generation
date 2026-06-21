class StringHelper:
    @staticmethod
    def compute_length(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return len(s)

if __name__ == '__main__':
    sample_input = "Alibaba Cloud Innovations"
    try:
        length_of_sample = StringHelper.compute_length(sample_input)
        print(f"The length of the string '{sample_input}' is: {length_of_sample}")
    except ValueError as e:
        print(e)