class ListReverser:
    @staticmethod
    def reverse_list(input_list):
        return input_list[::-1]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    reversed_values = ListReverser.reverse_list(sample_values)
    print(reversed_values)