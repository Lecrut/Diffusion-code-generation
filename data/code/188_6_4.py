class ReverseGenerator:
    @staticmethod
    def reverse_generator(lst):
        for i in range(len(lst) - 1, -1, -1):
            yield lst[i]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    gen = ReverseGenerator.reverse_generator(sample_list)
    for item in gen:
        print(item)