class StringReverser:
    RECURSION_LIMIT = 1000

    @staticmethod
    def reverse_string_recursive(s):
        if len(s) == 0:
            return s
        else:
            return StringReverser.reverse_string_recursive(s[1:]) + s[0]

    @staticmethod
    def reverse_string_slicing(s):
        return s[::-1]

if __name__ == '__main__':
    sample_string = "world"
    reverser = StringReverser()
    
    reversed_by_recursion = StringReverser.reverse_string_recursive(sample_string)
    print("Reversed by recursion:", reversed_by_recursion)
    
    reversed_by_slicing = StringReverser.reverse_string_slicing(sample_string)
    print("Reversed by slicing:", reversed_by_slicing)