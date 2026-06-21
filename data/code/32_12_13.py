class BinaryHexManager:
    @staticmethod
    def convert_binary_to_hex(binary_string):
        return hex(int(binary_string, 2))

if __name__ == '__main__':
    manager = BinaryHexManager()
    sample_values = ['1010', '11110000', '1', '1111111111111111']
    results = []
    for value in sample_values:
        result = manager.convert_binary_to_hex(value)
        results.append(result)
    for res in results:
        print(res)