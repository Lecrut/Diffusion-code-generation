class Sorter:
    def __init__(self, int_list):
        self.int_list = int_list

    def sort(self):
        return sorted(self.int_list)

if __name__ == '__main__':
    sample_values = [45, 23, 87, 12, 36, 90]
    sorter_instance = Sorter(sample_values)
    sorted_values = sorter_instance.sort()
    print(sorted_values)