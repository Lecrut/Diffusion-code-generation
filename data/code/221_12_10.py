SORTED_KEYS = ('first', 'second', 'third')

class SortedValues:
    def __init__(self, a, b, c):
        self.values = sorted([a, b, c])
    
    def get_sorted_values(self):
        return {key: value for key, value in zip(SORTED_KEYS, self.values)}

if __name__ == '__main__':
    values = SortedValues(3, 1, 2)
    print(values.get_sorted_values())