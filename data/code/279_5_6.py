class ListCycler:
    def cycle_and_print(self, data_list, start_index, end_index):
        if not data_list:
            return
        start = max(0, start_index)
        end = min(len(data_list), end_index + 1)
        for i in range(start, end):
            print(data_list[i])
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 60]
    cycler = ListCycler()
    print("Cycling from index 1 to 4:")
    cycler.cycle_and_print(my_list, 1, 4)
    print("\nCycling from index 0 to 2:")
    cycler.cycle_and_print(my_list, 0, 2)
    print("\nCycling from index 5 to 10 (out of bounds test):")
    cycler.cycle_and_print(my_list, 5, 10)
    print("\nCycling from index -5 to 1:")
    cycler.cycle_and_print(my_list, -5, 1)