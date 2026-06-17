class ListCycler:
    def cycle_and_print(self, data_list, start_index, end_index):
        for i in range(start_index, end_index + 1):
            if 0 <= i < len(data_list):
                print(data_list[i])
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 60]
    cycler = ListCycler()
    start = 1
    end = 4
    cycler.cycle_and_print(my_list, start, end)