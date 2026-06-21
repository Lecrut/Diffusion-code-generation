class ListCombiner:
    def __init__(self, initial_list):
        self.list = initial_list

    def append_elements(self, elements_to_add):
        self.list += elements_to_add

if __name__ == '__main__':
    combiner = ListCombiner([1, 2, 3])
    combiner.append_elements([4, 5, 6])
    print("Updated List:", combiner.list)