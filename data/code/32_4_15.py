class BinaryValidationError(ValueError):
    def __init__(self, message, char=''):
        self.char = char
        super().__init__(message)

def binary_to_hexadecimal(binary_str):
    if not binary_str:
        raise BinaryValidationError("Input cannot be empty.")
    
    for char in binary_str:
        if char not in '01':
            raise BinaryValidationError(f"Invalid character '{char}' in binary input.", char=char)
            
    hex_str = hex(int(binary_str, 2))[2:]
    return hex_str

if __name__ == '__main__':
    result = binary_to_hexadecimal('101010')
    print(result)