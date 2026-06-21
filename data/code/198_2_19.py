class NumericStringAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_minimum(self):
        if not self.data:
            raise ValueError("List cannot be empty")
        minimum = float(self.data[0])
        for item in self.data[1:]:
            if float(item) < minimum:
                minimum = float(item)
        return minimum

if __name__ == '__main__':
    list1 = ['5', '2', '8', '1', '9']
    analyzer1 = NumericStringAnalyzer(list1)
    print(f"Minimum of {list1}: {analyzer1.get_minimum()}")
    
    list2 = ['-10.5', '0.0', '-5', '3.14']
    analyzer2 = NumericStringAnalyzer(list2)
    print(f"Minimum of {list2}: {analyzer2.get_minimum()}")