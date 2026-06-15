class Sorter:
    def sort_list(self, data):
        data.sort()
if __name__ == '__main__':
    my_list = [5, 2, 8, 1, 9, 4]
    sorter = Sorter()
    sorter.sort_list(my_list)
    print(my_list)