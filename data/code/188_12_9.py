class ListReverser:
    def __init__(self, input_list):
        self.input_list = input_list

    def reverse_builtin(self):
        return list(reversed(self.input_list))

    def reverse_method(self):
        new_list = self.input_list[:]
        new_list.reverse()
        return new_list

    def reverse_manual(self):
        reversed_list = []
        for item in self.input_list:
            reversed_list.insert(0, item)
        return reversed_list

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    
    print("Original List:", sample_list)
    print("-" * 30)
    print("Reversed (Builtin):", reverser.reverse_builtin())
    print("Reversed (reverse()):", reverser.reverse_method())
    print("Reversed (Manual):", reverser.reverse_manual())