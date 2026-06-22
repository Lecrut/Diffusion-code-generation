class MinMaxUtil:
    @staticmethod
    def find_min_max(data_tuple):
        if not data_tuple:
            return None, None
        
        current_min = data_tuple[0]
        current_max = data_tuple[0]
        
        for item in data_tuple:
            if item < current_min:
                current_min = item
            if item > current_max:
                current_max = item
                
        return current_min, current_max

if __name__ == '__main__':
    sample_data1 = (10, 5, 20, 8, 15)
    min_val1, max_val1 = MinMaxUtil.find_min_max(sample_data1)
    print(f"Data: {sample_data1}, Minimum: {min_val1}, Maximum: {max_val1}")
    
    sample_data2 = (-5, 100, 0, -50)
    min_val2, max_val2 = MinMaxUtil.find_min_max(sample_data2)
    print(f"Data: {sample_data2}, Minimum: {min_val2}, Maximum: {max_val2}")