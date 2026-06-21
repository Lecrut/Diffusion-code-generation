class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        char_list = list(self.text)
        left, right = 0, len(char_list) - 1
        while left < right:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        return ''.join(char_list)

if __name__ == '__main__':
    sample_text1 = 'hello'
    sample_text2 = 'world'
    
    reverser1 = StringReverser(sample_text1)
    print(reverser1.reverse())
    
    reverser2 = StringReverser(sample_text2)
    print(reverser2.reverse())