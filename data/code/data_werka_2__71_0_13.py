class ListProcessor:
    _ODD_INDEX_OFFSET = 0
    _EVEN_INDEX_OFFSET = -1

    @staticmethod
    def find_middle_element(data):
        length = len(data)
        if length == 0:
            raise ValueError("Input list must not be empty")
        
        center = length // 2
        
        if length % 2 == 1:
            slice_start = center + ListProcessor._ODD_INDEX_OFFSET
            slice_end = center + 2
            middle_part = data[slice_start:slice_end]
            return middle_part[0]
        else:
            slice_start = center + ListProcessor._EVEN_INDEX_OFFSET
            slice_end = center + 1
            middle_part = data[slice_start:slice_end]
            return (middle_part[0] + middle_part[1]) / 2

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70]
    result = ListProcessor.find_middle_element(sample_data)
    print(result)
    
    sample_data_even = [10, 20, 30, 40, 50, 60]
    result_even = ListProcessor.find_middle_element(sample_data_even)
    print(result_even)