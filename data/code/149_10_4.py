class ListReverser:
    def reverse_list(self, input_list):
        return input_list[::-1]

if __name__ == '__main__':
    reverser = ListReverser()
    sample_values = [1, 2, 3, 4, 5]
    reversed_values = reverser.reverse_list(sample_values)
    print(reversed_values)