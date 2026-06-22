class NumberComparator:
    def compare(self, a, b):
        if not isinstance(a, str) or not isinstance(b, str):
            raise ValueError("Both inputs must be strings representing numbers.")
        
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        for i in range(max_len):
            if a[i] > b[i]:
                return True
            elif a[i] < b[i]:
                return False
        
        return a == b

if __name__ == '__main__':
    comparator = NumberComparator()
    print(comparator.compare("12345", "67890"))
    print(comparator.compare("10000", "9999"))
    print(comparator.compare("12345", "12345"))