class StringReverser:
    def reverse_string_recursive(self, s):
        if len(s) == 0:
            return s
        else:
            return self.reverse_string_recursive(s[1:]) + s[0]

    def reverse_string_slicing(self, s):
        return s[::-1]

if __name__ == '__main__':
    sample_string = "example"
    reverser = StringReverser()
    
    reversed_by_recursion = reverser.reverse_string_recursive(sample_string)
    reversed_by_slicing = reverser.reverse_string_slicing(sample_string)
    
    print("Reversed by recursion:", reversed_by_recursion)
    print("Reversed by slicing:", reversed_by_slicing)