class MinMaxFinder:
    @staticmethod
    def find_min_max(list1, list2):
        combined = list1 + list2
        if not combined:
            return None, None
        
        min_val = combined[0]
        max_val = combined[0]
        
        for item in combined[1:]:
            if item < min_val:
                min_val = item
            if item > max_val:
                max_val = item
        
        return min_val, max_val

if __name__ == '__main__':
    list1 = [3, 5, 7, 9]
    list2 = [2, 4, 6, 8]
    min_value, max_value = MinMaxFinder.find_min_max(list1, list2)
    print(f"Minimum value: {min_value}, Maximum value: {max_value}")