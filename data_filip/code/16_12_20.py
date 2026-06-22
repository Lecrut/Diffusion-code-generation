class RunLengthEncoder:
    def encode(self, input_string):
        if not input_string:
            return []
        
        result = []
        current_char = input_string[0]
        count = 1
        
        for i in range(1, len(input_string)):
            if input_string[i] == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = input_string[i]
                count = 1
        
        result.append((current_char, count))
        return result

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    test_string = "aaabbccccd"
    encoded_result = encoder.encode(test_string)
    print(encoded_result)
    empty_string = ""
    empty_result = encoder.encode(empty_string)
    print(empty_result)
    single_char_string = "z"
    single_result = encoder.encode(single_char_string)
    print(single_result)