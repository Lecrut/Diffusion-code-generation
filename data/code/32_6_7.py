from typing import List

class BinaryConverter:
    @staticmethod
    def binary_sequence_to_hex(bits: List[int]) -> str:
        if not bits:
            return "0"
        
        bit_string = "".join(str(b) for b in bits)
        if not all(c in "01" for c in bit_string):
            raise ValueError("Sequence must contain only 0s and 1s")
        
        if not bit_string:
            return "0"
        
        number = int(bit_string, 2)
        return hex(number)[2:].upper()

if __name__ == '__main__':
    converter = BinaryConverter()
    sample_bits_1 = [0, 1, 1, 0, 1, 0, 1, 1]
    result_1 = converter.binary_sequence_to_hex(sample_bits_1)
    print(result_1)
    
    sample_bits_2 = [1, 1, 1, 1, 1, 1, 1, 1]
    result_2 = converter.binary_sequence_to_hex(sample_bits_2)
    print(result_2)
    
    sample_bits_3 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]
    result_3 = converter.binary_sequence_to_hex(sample_bits_3)
    print(result_3)