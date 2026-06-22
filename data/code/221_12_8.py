class NumberSorter:
    def __init__(self, x, y, z):
        self.values = sorted([x, y, z])
    
    def get_sorted_values(self):
        return self.values

if __name__ == '__main__':
    sorter = NumberSorter(5, 2, 8)
    print(sorter.get_sorted_values())