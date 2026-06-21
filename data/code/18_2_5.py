import itertools

class RunLengthEncoder:
    BUFFER_LIMIT = 1000

    def encode(self, text):
        if not text:
            return ""
        encoded_parts = []
        for char, group in itertools.groupby(text):
            run_length = len(list(group))
            encoded_parts.append(str(run_length))
            encoded_parts.append(char)
        return "".join(encoded_parts)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "aaabbcbbbb"
    result = encoder.encode(sample_input)
    print(result)
    
    sample_input_2 = "hello"
    result_2 = encoder.encode(sample_input_2)
    print(result_2)
    
    sample_input_3 = ""
    result_3 = encoder.encode(sample_input_3)
    print(result_3)