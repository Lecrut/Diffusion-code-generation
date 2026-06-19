class Reverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return self.input_string[::-1]

if __name__ == '__main__':
    SAMPLE_STRING = "Hello, 世界!"
    reverser_instance = Reverser(SAMPLE_STRING)
    reversed_result = reverser_instance.reverse()
    print(reversed_result)