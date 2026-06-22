class RLEncoder:
    def __init__(self, input_string):
        self.input_string = input_string

    def encode(self):
        if not self.input_string:
            return ""
        encoded_parts = []
        current_char = self.input_string[0]
        count = 1
        total_length = len(self.input_string)
        for index in range(1, total_length):
            next_char = self.input_string[index]
            if next_char == current_char:
                count += 1
            else:
                encoded_parts.append(current_char + str(count))
                current_char = next_char
                count = 1
        encoded_parts.append(current_char + str(count))
        return "".join(encoded_parts)

if __name__ == '__main__':
    test_data = 'AAAAABBBBCCCCCDDDDDDDDDEEEEEEEFFFGGGHHHHIIJJ'
    encoder_instance = RLEncoder(test_data)
    print(encoder_instance.encode())