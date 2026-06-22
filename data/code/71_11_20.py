class ListAnalyzer:
    _OFFSET = 0

    def get_middle_value(self, data):
        if not data:
            raise ValueError("List must not be empty")
        
        n = len(data)
        is_odd = n % 2 == 1
        
        if is_odd:
            index = n // 2 + self._OFFSET
            return data[index]
        
        mid_right = n // 2 + self._OFFSET
        mid_left = mid_right - 1
        val_left = data[mid_left]
        val_right = data[mid_right]
        
        if isinstance(val_left, float) or isinstance(val_right, float):
            return (val_left + val_right) / 2.0
        
        return (val_left + val_right) / 2

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    odd_list = [1, 3, 5, 7, 9]
    even_list = [10, 20, 30, 40]
    
    odd_result = analyzer.get_middle_value(odd_list)
    print(odd_result)
    
    even_result = analyzer.get_middle_value(even_list)
    print(even_result)