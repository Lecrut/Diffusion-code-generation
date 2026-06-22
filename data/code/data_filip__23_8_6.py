import sys
from collections import deque

SAMPLE_INPUT = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"

def _process_group(char, count):
    return str(count) + char

def run_length_encode(text):
    if not text:
        return ""
    
    buffer = deque()
    current = text[0]
    runs = 1
    
    for index in range(1, len(text)):
        char = text[index]
        if char == current:
            runs += 1
        else:
            buffer.append(_process_group(current, runs))
            current = char
            runs = 1
    
    buffer.append(_process_group(current, runs))
    
    return "".join(buffer)

class Encoder:
    def __init__(self, data):
        self.data = data
    
    def encode(self):
        return run_length_encode(self.data)

if __name__ == '__main__':
    sample_text = SAMPLE_INPUT
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)
    
    instance = Encoder(sample_text)
    instance_result = instance.encode()
    print(instance_result)