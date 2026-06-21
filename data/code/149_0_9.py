def reverse_list(input_list):
    return input_list[::-1]

class ListReverser:
    def __init__(self, input_list):
        self.input_list = input_list
    
    def get_original(self):
        return self.input_list
    
    def get_reversed(self):
        return self.input_list[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    original_list = reverser.get_original()
    reversed_list = reverser.get_reversed()
    print("Original list:", original_list)
    print("Reversed list:", reversed_list)