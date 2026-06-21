def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    middle_index = len(lst) // 2
    return lst[middle_index]

class ListProcessor:
    def __init__(self, data):
        self.data = data

    def get_middle_element(self):
        return find_middle_element(self.data)

if __name__ == '__main__':
    sample_odd_list = [10, 20, 30, 40, 50]
    sample_even_list = [5, 15, 25, 35, 45, 55]

    processor_odd = ListProcessor(sample_odd_list)
    processor_even = ListProcessor(sample_even_list)

    print(processor_odd.get_middle_element())
    print(processor_even.get_middle_element())