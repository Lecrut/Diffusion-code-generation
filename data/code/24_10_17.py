class RLEProcessor:
    ENCODING_PREFIX = "RLE:"
    
    def _build_compressed_pairs(self, source):
        if len(source) == 0:
            return []
        
        result_pairs = []
        working_char = source[0]
        running_count = 1
        
        for index in range(1, len(source)):
            char_at_index = source[index]
            if char_at_index == working_char:
                running_count += 1
            else:
                result_pairs.append((running_count, working_char))
                working_char = char_at_index
                running_count = 1
        
        result_pairs.append((running_count, working_char))
        return result_pairs

    def compress(self, raw_text):
        if raw_text is None or len(raw_text) == 0:
            return self.ENCODING_PREFIX
            
        pairs = self._build_compressed_pairs(raw_text)
        formatted_parts = []
        
        for count, char in pairs:
            formatted_parts.append(str(count))
            formatted_parts.append(char)
            
        return self.ENCODING_PREFIX + "".join(formatted_parts)

    def decompress(self, encoded_text):
        if encoded_text is None:
            return ""
            
        if not encoded_text.startswith(self.ENCODING_PREFIX):
            raise ValueError("Invalid encoding format")
            
        payload = encoded_text[len(self.ENCODING_PREFIX):]
        
        if len(payload) == 0:
            return ""
            
        expanded_chars = []
        i = 0
        while i < len(payload):
            count_str = ""
            while i < len(payload) and payload[i].isdigit():
                count_str += payload[i]
                i += 1
                
            if len(count_str) == 0:
                break
                
            run_length = int(count_str)
            
            if i < len(payload):
                symbol = payload[i]
                expanded_chars.append(symbol * run_length)
                i += 1
            else:
                break
                
        return "".join(expanded_chars)

if __name__ == '__main__':
    processor = RLEProcessor()
    
    test_string_one = "AAABBBCCDAA"
    test_string_two = "XYZXYZ"
    test_string_three = "MMMMMNNNO"
    
    compressed_one = processor.compress(test_string_one)
    decompressed_one = processor.decompress(compressed_one)
    
    print(compressed_one)
    print(decompressed_one)
    
    compressed_two = processor.compress(test_string_two)
    decompressed_two = processor.decompress(compressed_two)
    
    print(compressed_two)
    print(decompressed_two)
    
    compressed_three = processor.compress(test_string_three)
    decompressed_three = processor.decompress(compressed_three)
    
    print(compressed_three)
    print(decompressed_three)
    
    empty_compressed = processor.compress("")
    print(empty_compressed)
    
    single_compressed = processor.compress("A")
    single_decompressed = processor.decompress(single_compressed)
    print(single_decompressed)