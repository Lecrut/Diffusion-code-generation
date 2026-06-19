class LengthComparator:
    EQUAL = 'equal'
    LEN1_GREATER = 'len1 is greater'
    LEN2_SMALLER = 'len2 is smaller'

    @staticmethod
    def compare(len1, len2):
        if not isinstance(len1, (int, float)) or not isinstance(len2, (int, float)):
            raise ValueError("Both inputs must be numbers")
        
        if len1 == len2:
            return LengthComparator.EQUAL
        elif len1 > len2:
            return LengthComparator.LEN1_GREATER
        else:
            return LengthComparator.LEN2_SMALLER

if __name__ == '__main__':
    length1 = 35
    length2 = 20
    try:
        result = LengthComparator.compare(length1, length2)
        print(result)
    except ValueError as e:
        print(e)