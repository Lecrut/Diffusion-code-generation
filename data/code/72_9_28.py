class ComparisonResult:
    DIFFERENCE = "difference"
    GREATER = "greater than"
    LESS = "less than"
    EQUAL = "equal"
    INVALID = "invalid index"

    @staticmethod
    def _validate_indices(lst, i1, i2):
        length = len(lst)
        if not (0 <= i1 < length) or not (0 <= i2 < length):
            return False
        return True

    @staticmethod
    def _get_values(lst, i1, i2):
        return lst[i1], lst[i2]

def compare_elements(lst, idx1, idx2):
    if not isinstance(lst, list):
        return ComparisonResult.INVALID
    
    if not ComparisonResult._validate_indices(lst, idx1, idx2):
        return ComparisonResult.INVALID
    
    val1, val2 = ComparisonResult._get_values(lst, idx1, idx2)
    
    if val1 > val2:
        return ComparisonResult.GREATER
    elif val1 < val2:
        return ComparisonResult.LESS
    else:
        return ComparisonResult.EQUAL

if __name__ == '__main__':
    data = [100, 200, 150, 150]
    res1 = compare_elements(data, 1, 0)
    print(res1)
    
    res2 = compare_elements(data, 2, 3)
    print(res2)
    
    res3 = compare_elements(data, 0, 5)
    print(res3)