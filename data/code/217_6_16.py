class NumberComparator:
    MAX_DIGIT_VALUE = '9'
    
    @staticmethod
    def compare_numbers(a, b):
        if not isinstance(a, str) or not isinstance(b, str):
            raise ValueError("Both inputs must be strings representing numbers.")
        
        len_a, len_b = len(a), len(b)
        max_len = max(len_a, len_b)
        
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        for i in range(max_len):
            if a[i] > b[i]:
                return True
            elif a[i] < b[i]:
                return False
        
        return False

if __name__ == '__main__':
    print(NumberComparator.compare_numbers('1234567890', '123456789'))
    print(NumberComparator.compare_numbers('123456789', '1234567890'))
    print(NumberComparator.compare_numbers('0', '0'))