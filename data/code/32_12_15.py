class BinaryHexManager:
    BASE = 2
    HEX_PREFIX = '0x'

    def __init__(self):
        self._cache = {}

    def convert(self, binary_input):
        if not isinstance(binary_input, str):
            raise TypeError("Input must be a string")
        clean_input = binary_input.strip()
        if not clean_input:
            return self.HEX_PREFIX + '0'
        if clean_input in self._cache:
            return self._cache[clean_input]
        for char in clean_input:
            if char not in ('0', '1'):
                raise ValueError("Invalid binary character detected")
        decimal_val = int(clean_input, self.BASE)
        hex_val = hex(decimal_val)
        self._cache[clean_input] = hex_val
        return hex_val

    def clear_cache(self):
        self._cache.clear()

    def get_cache_size(self):
        return len(self._cache)

if __name__ == '__main__':
    manager = BinaryHexManager()
    test_cases = ['1010', '11110000', '0', '110011001100']
    for case in test_cases:
        output = manager.convert(case)
        print(f"{case} -> {output}")
    second_test = "10111111101"
    result = manager.convert(second_test)
    print(f"{second_test} -> {result}")
    manager.clear_cache()
    print(manager.get_cache_size())