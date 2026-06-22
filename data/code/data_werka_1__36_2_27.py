class StringReverser:
    def reverse(self, text):
        return ''.join(reversed(text))

if __name__ == '__main__':
    reverser = StringReverser()
    SAMPLE_TEXT_1 = "example"
    REVERSED_TEXT_1 = reverser.reverse(SAMPLE_TEXT_1)
    print(f"Original: {SAMPLE_TEXT_1}, Reversed: {REVERSED_TEXT_1}")
    
    SAMPLE_TEXT_2 = "test123"
    REVERSED_TEXT_2 = reverser.reverse(SAMPLE_TEXT_2)
    print(f"Original: {SAMPLE_TEXT_2}, Reversed: {REVERSED_TEXT_2}")
    
    SAMPLE_TEXT_3 = "OpenAI"
    REVERSED_TEXT_3 = reverser.reverse(SAMPLE_TEXT_3)
    print(f"Original: {SAMPLE_TEXT_3}, Reversed: {REVERSED_TEXT_3}")