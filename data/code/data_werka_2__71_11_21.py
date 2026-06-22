class ListAnalyzer:
    def get_middle_value(self, data):
        if not data:
            raise ValueError("List must not be empty")
        count = len(data)
        index = (count - 1) // 2
        return data[index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    numbers = [5, 15, 25, 35, 45, 55, 65]
    middle = analyzer.get_middle_value(numbers)
    print(middle)