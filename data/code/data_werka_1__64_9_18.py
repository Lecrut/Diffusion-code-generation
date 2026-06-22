class Finder:
    def __init__(self, data):
        self.data = data

    def find_final_index(self, target):
        last_index = -1
        for i in range(len(self.data)):
            if self.data[i] == target:
                last_index = i
        return last_index

if __name__ == '__main__':
    my_finder = Finder([1, 5, 2, 8, 5, 3, 5, 9])
    target_value = 5
    final_index = my_finder.find_final_index(target_value)
    print(final_index)

    another_finder = Finder([10, 20, 30, 20, 40, 20])
    target_value_2 = 20
    final_index_2 = another_finder.find_final_index(target_value_2)
    print(final_index_2)

    yet_another_finder = Finder([1, 2, 3, 4])
    target_value_3 = 99
    final_index_3 = yet_another_finder.find_final_index(target_value_3)
    print(final_index_3)