class ListAnalyzer:
    @staticmethod
    def get_minimum(data):
        if not data:
            raise ValueError("List cannot be empty")
        minimum = data[0]
        for item in data[1:]:
            if item < minimum:
                minimum = item
        return minimum

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    min_value1 = ListAnalyzer.get_minimum(list1)
    print(f"Minimum of {list1}: {min_value1}")
    
    list2 = [-10, 0, -5, 3]
    min_value2 = ListAnalyzer.get_minimum(list2)
    print(f"Minimum of {list2}: {min_value2}")