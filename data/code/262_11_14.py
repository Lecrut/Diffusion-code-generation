class MinMaxFinder:
    @staticmethod
    def find_min_max(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        minimum = min(data)
        maximum = max(data)
        return (minimum, maximum)

if __name__ == '__main__':
    finder = MinMaxFinder()
    list1 = [3, 1, 4, 1, 5, 9, 2, 6]
    result1 = finder.find_min_max(list1)
    print(f"List: {list1}, Min: {result1[0]}, Max: {result1[1]}")
    
    list2 = [-10, 0, 5, -20, 100]
    result2 = finder.find_min_max(list2)
    print(f"List: {list2}, Min: {result2[0]}, Max: {result2[1]}")