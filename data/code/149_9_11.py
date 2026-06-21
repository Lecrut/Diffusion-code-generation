class ListReverser:
    def __init__(self, mixed_list):
        self.mixed_list = mixed_list

    def reverse(self):
        return self.mixed_list[::-1]

if __name__ == '__main__':
    sample = [1, 'a', 3.14, True, None]
    reverser = ListReverser(sample)
    reversed_sample = reverser.reverse()
    print(reversed_sample)