class RLECodec:
    def __init__(self):
        self.default_run_limit = 65535

    def compress(self, source_string):
        if not source_string:
            return ""
        
        def chunked_compression_generator(text):
            length = len(text)
            if length == 0:
                return
            
            current_char = text[0]
            current_count = 1
            
            for index in range(1, length):
                next_char = text[index]
                if next_char == current_char and current_count < self.default_run_limit:
                    current_count += 1
                else:
                    yield f"{current_count}{current_char}"
                    current_char = next_char
                    current_count = 1
            
            yield f"{current_count}{current_char}"
        
        return "".join(chunked_compression_generator(source_string))

    def decompress(self, compressed_string):
        if not compressed_string:
            return ""
        
        def parsing_generator(code):
            length = len(code)
            index = 0
            while index < length:
                number_end = index
                while number_end < length and not code[number_end].isalpha():
                    number_end += 1
                
                count_str = code[index:number_end]
                if count_str:
                    count = int(count_str)
                else:
                    count = 1
                    number_end = index
                
                if number_end < length:
                    char = code[number_end]
                    yield char * count
                    index = number_end + 1
                else:
                    break
        
        return "".join(parsing_generator(compressed_string))

if __name__ == '__main__':
    codec_instance = RLECodec()
    
    sample_input_1 = "AAABBBCCCCD"
    sample_input_2 = ""
    sample_input_3 = "ABCDEF"
    sample_input_4 = "X"
    
    compressed_1 = codec_instance.compress(sample_input_1)
    decompressed_1 = codec_instance.decompress(compressed_1)
    
    compressed_2 = codec_instance.compress(sample_input_2)
    decompressed_2 = codec_instance.decompress(compressed_2)
    
    compressed_3 = codec_instance.compress(sample_input_3)
    decompressed_3 = codec_instance.decompress(compressed_3)
    
    compressed_4 = codec_instance.compress(sample_input_4)
    decompressed_4 = codec_instance.decompress(compressed_4)
    
    print(compressed_1)
    print(decompressed_1)
    print(compressed_2)
    print(decompressed_2)
    print(compressed_3)
    print(decompressed_3)
    print(compressed_4)
    print(decompressed_4)