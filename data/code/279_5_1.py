class MyList:
    def __init__(self, data):
        self.data = data
    def cycle_and_print(self, start_index, end_index):
        for i in range(start_index, end_index + 1):
            if 0 <= i < len(self.data):
                print(self.data[i])
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    my_list = MyList(sample_list)
    my_list.cycle_and_print(1, 4)