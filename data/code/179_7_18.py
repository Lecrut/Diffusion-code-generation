class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_word_order(self):
        words = self.input_string.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == '__main__':
    reverser_instance = StringReverser("Data Science is fun")
    result = reverser_instance.reverse_word_order()
    print(result)