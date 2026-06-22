class Sorter:
    @staticmethod
    def sort_sequence(a, b, c):
        return sorted([a, b, c], key=lambda x: x)

if __name__ == '__main__':
    sample_values = (10, 5, 20)
    sorted_sequence = Sorter.sort_sequence(*sample_values)
    print(sorted_sequence)