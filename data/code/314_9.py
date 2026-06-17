class MyList:
    def __init__(self, data):
        self.data = data
    def calculate_sum(self):
        return sum(self.data)
if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    my_list = MyList(sample_list)
    result = my_list.calculate_sum()
    print(result)