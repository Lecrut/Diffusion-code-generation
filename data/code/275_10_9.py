class StringReverser:
    @staticmethod
    def reverse_string(s):
        reversed_str = ''
        for char in s:
            reversed_str = char + reversed_str
        return reversed_str

    @staticmethod
    def process_strings(string_list):
        for s in string_list:
            print(StringReverser.reverse_string(s))

if __name__ == '__main__':
    sample_values = ["Python", "is", "awesome!"]
    StringReverser.process_strings(sample_values)