class BinaryValidationError(Exception):
    def __init__(self, message="Invalid binary input"):
        self.message = message
        super().__init__(self.message)

def binary_to_hex(binary_str):
    valid_chars = set('01')
    if not binary_str:
        raise BinaryValidationError("Input cannot be empty")
    
    for char in binary_str:
        if char not in valid_chars:
            raise BinaryValidationError(f"Invalid character '{char}' found in binary string")
    
    decimal_value = int(binary_str, 2)
    hex_str = hex(decimal_value)[2:].upper()
    
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str
        
    return hex_str

if __name__ == '__main__':
    sample_binary = "10101100"
    result = binary_to_hex(sample_binary)
    print(result)