class List:
    def __init__(self, data):
        self.data = data
    def get_middle(self):
        n = len(self.data)
        middle_index = n // 2
        return self.data[middle_index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    my_list = List(sample_list)
    middle_element = my_list.get_middle()
    print(middle_element)
    sample_list_even = [1, 2, 3, 4]
    my_list_even = List(sample_list_even)
    middle_element_even = my_list_even.get_middle()
    print(middle_element_even)
    sample_list_odd = [100, 200, 300]
    my_list_odd = List(sample_list_odd)
    middle_element_odd = my_list_odd.get_middle()
    print(middle_element_odd)