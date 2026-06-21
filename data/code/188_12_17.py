class ListReverser:
    def __init__(self, input_list):
        self.input_list = input_list

    def reverse_builtin(self):
        return list(reversed(self.input_list))

    def reverse_method(self):
        new_list = self.input_list[:]
        new_list.reverse()
        return new_list

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    print("Original List:", sample_list)
    reversed_builtin = reverser.reverse_builtin()
    print("Reversed (Built-in):", reversed_builtin)
    reversed_method = reverser.reverse_method()
    print("Reversed (reverse()):", reversed_method)