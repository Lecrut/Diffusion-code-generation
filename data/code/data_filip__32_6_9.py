from typing import TypeVar

T = TypeVar('T')

class BinaryConverter:
    @staticmethod
    def to_hex(binary_sequence: str) -> str:
        if not binary_sequence:
            return ""
        
        if not all(c in '01' for c in binary_sequence):
            raise ValueError("Input must contain only '0' and '1'")
        
        padding = (4 - len(binary_sequence) % 4) % 4
        padded_sequence = "0" * padding + binary_sequence
        
        hex_chars = []
        for i in range(0, len(padded_sequence), 4):
            nibble = padded_sequence[i:i+4]
            value = 0
            for bit in nibble:
                value = (value << 1) | int(bit)
            hex_chars.append(format(value, 'x'))
        
        return "".join(hex_chars)

if __name__ == '__main__':
    converter = BinaryConverter()
    sample_binary = "110101101111"
    result = converter.to_hex(sample_binary)
    print(result)
    
    another_sample = "1010"
    second_result = converter.to_hex(another_sample)
    print(second_result)