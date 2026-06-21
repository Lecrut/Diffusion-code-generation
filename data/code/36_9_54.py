class StringReverser:
    def __init__(self):
        self.special_chars_map = {
            '!': '1',
            '@': '2',
            '#': '3',
            '$': '4',
            '%': '5'
        }
    
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        reversed_text = []
        for char in reversed(text):
            if char in self.special_chars_map:
                reversed_text.append(self.special_chars_map[char])
            else:
                reversed_text.append(char)
        
        return ''.join(reversed_text)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text1 = "Hello, World!"
    sample_text2 = "Alibaba Cloud @#%$"
    reversed_text1 = reverser.reverse(sample_text1)
    print(reversed_text1)
    reversed_text2 = reverser.reverse(sample_text2)
    print(reversed_text2)