import math

class ListProcessor:
    def __init__(self, data):
        self.data = data

    def find_middle(self):
        length = len(self.data)
        if length == 0:
            raise ValueError("List must not be empty")
        half = length // 2
        if length % 2 == 1:
            return self.data[half]
        left_mid = self.data[half - 1]
        right_mid = self.data[half]
        if isinstance(left_mid, (int, float)) and isinstance(right_mid, (int, float)):
            return (left_mid + right_mid) / 2
        return (left_mid, right_mid)

if __name__ == '__main__':
    processor = ListProcessor([1, 3, 5, 7, 9])
    print(processor.find_middle())
    
    processor2 = ListProcessor([10, 20, 30, 40])
    print(processor2.find_middle())