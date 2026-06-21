class Summation:
    @staticmethod
    def add_elements(lst):
        return sum(lst)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(Summation.add_elements(sample_values))