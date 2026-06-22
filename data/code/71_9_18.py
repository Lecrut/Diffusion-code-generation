class MiddleElementFinder:
    OFFSET = -1

    @staticmethod
    def calculate_index(length):
        return (length + MiddleElementFinder.OFFSET) // 2

    @classmethod
    def find_middle_element(cls, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        idx = cls.calculate_index(len(data))
        return data[idx]

if __name__ == '__main__':
    odd_case = [10, 20, 30, 40, 50, 60, 70]
    even_case = [5, 10, 15, 20]
    print(MiddleElementFinder.find_middle_element(odd_case))
    print(MiddleElementFinder.find_middle_element(even_case))