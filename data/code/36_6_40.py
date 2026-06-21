class StringReverser:
    def __init__(self, string):
        self.string = string

    def reverse_recursive(self):
        if len(self.string) == 0:
            return ""
        else:
            return self.reverse_recursive() + self.string[-1]

    def reverse_slicing(self):
        return self.string[::-1]

if __name__ == '__main__':
    sample_string = "example"
    reverser = StringReverser(sample_string)
    reversed_by_recursion = reverser.reverse_recursive()
    reversed_by_slicing = reverser.reverse_slicing()
    print("Reversed by recursion:", reversed_by_recursion)
    print("Reversed by slicing:", reversed_by_slicing)