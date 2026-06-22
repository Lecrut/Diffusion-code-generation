class NumberComparer:
    @staticmethod
    def compare_numbers(a: str, b: str) -> bool:
        len_a, len_b = len(a), len(b)
        
        if len_a > len_b:
            return True
        elif len_a < len_b:
            return False
        
        for i in range(len_a):
            if a[i] > b[i]:
                return True
            elif a[i] < b[i]:
                return False
        
        return False

if __name__ == '__main__':
    print(NumberComparer.compare_numbers("1234567890", "12345"))
    print(NumberComparer.compare_numbers("1234567890", "1234567890"))
    print(NumberComparer.compare_numbers("1234567890", "1234567891"))