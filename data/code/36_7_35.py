class StringReverser:
    RECURSIVE_COUNT = 0

    @staticmethod
    def reverse_string_recursive(s):
        StringReverser.RECURSIVE_COUNT += 1
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
    
    reversed_by_recursion = reverser.reverse_string_recursive(sample_string)
    print("Reversed by recursion:", reversed_by_recursion)
    
    reversed_by_slicing = reverser.reverse_string_slicing(sample_string)
    print("Reversed by slicing:", reversed_by_slicing)

    print(f"Recursive calls made: {StringReverser.RECURSIVE_COUNT}")