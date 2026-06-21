class ReverseGenerator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    @staticmethod
    def reverse_generator(lst):
        for i in range(len(lst) - 1, -1, -1):
            yield lst[i]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    rg = ReverseGenerator(sample_list)
    for item in rg.reverse_generator(sample_list):
        print(item)