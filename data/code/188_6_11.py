class ReverseGenerator:
    @staticmethod
    def reverse_generator(lst):
        for i in range(len(lst) - 1, -1, -1):
            yield lst[i]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    for item in ReverseGenerator.reverse_generator(sample_list):
        print(item)