class ListCycler:
    def cycle_and_print(self, data_list, start_index, end_index):
        if not data_list:
            return
        n = len(data_list)
        start = max(0, start_index)
        end = min(n, end_index)
        for i in range(start, end):
            print(data_list[i])
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 60]
    cycler = ListCycler()
    print("Cycling from index 1 to 4:")
    cycler.cycle_and_print(my_list, 1, 4)
    print("\nCycling from index 0 to 2:")
    cycler.cycle_and_print(my_list, 0, 2)
    print("\nCycling from index 5 to 6 (out of bounds test):")
    cycler.cycle_and_print(my_list, 5, 6)
    print("\nCycling from index -1 to 3 (negative start test):")
    cycler.cycle_and_print(my_list, -1, 3)