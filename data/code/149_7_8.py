class ListReverser:
    @staticmethod
    def reverse_integers(integer_list):
        return integer_list[::-1]

if __name__ == '__main__':
    sample_values = [4, 3, 2, 1]
    reversed_result = ListReverser.reverse_integers(sample_values)
    print(reversed_result)