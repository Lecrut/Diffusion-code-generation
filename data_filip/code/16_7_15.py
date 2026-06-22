class BinaryRunLengthEncoder:
    SAMPLE_DATA = "00111000110000"

    @staticmethod
    def encode(binary_string):
        if not binary_string:
            return []
        counts = []
        current_char = binary_string[0]
        count = 1
        for index in range(1, len(binary_string)):
            if binary_string[index] == current_char:
                count += 1
            else:
                counts.append(count)
                current_char = binary_string[index]
                count = 1
        counts.append(count)
        return counts

if __name__ == '__main__':
    sample_binary = "00111000110000"
    encoder_instance = BinaryRunLengthEncoder()
    print(BinaryRunLengthEncoder.encode(sample_binary))