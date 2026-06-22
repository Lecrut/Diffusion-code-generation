class StringReverser:
    def reverse(self, text):
        reversed_text = ""
        for char in text:
            reversed_text = char + reversed_text
        return reversed_text

if __name__ == '__main__':
    reverser = StringReverser()
    
    sample_string_1 = "example"
    result_1 = reverser.reverse(sample_string_1)
    print(f"Original: {sample_string_1}, Reversed: {result_1}")
    
    sample_string_2 = "testcase"
    result_2 = reverser.reverse(sample_string_2)
    print(f"Original: {sample_string_2}, Reversed: {result_2}")
    
    sample_string_3 = "openai"
    result_3 = reverser.reverse(sample_string_3)
    print(f"Original: {sample_string_3}, Reversed: {result_3}")