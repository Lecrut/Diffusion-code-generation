class BinaryHexManager:
    PREFIX = '0x'

    @staticmethod
    def convert_to_hex(binary_string):
        decimal_value = int(binary_string, 2)
        return BinaryHexManager.PREFIX + format(decimal_value, 'x')

    def convert_batch(self, binary_strings):
        results = []
        for bs in binary_strings:
            results.append(BinaryHexManager.convert_to_hex(bs))
        return results

if __name__ == '__main__':
    sample_binary = '101101'
    manager = BinaryHexManager()
    result = manager.convert_to_hex(sample_binary)
    print(result)
    sample_batch = ['101', '1101', '0']
    batch_result = manager.convert_batch(sample_batch)
    print(batch_result)