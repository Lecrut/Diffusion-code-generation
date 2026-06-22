class Comparator:
    RESULT_GREATER = "greater than"
    RESULT_LESS = "less than"
    RESULT_EQUAL = "equal"
    RESULT_ERROR = "index out of bounds"

    @staticmethod
    def _validate_indices(length, idx1, idx2):
        if not (0 <= idx1 < length and 0 <= idx2 < length):
            return False
        return True

    @staticmethod
    def compare_elements(data, index_a, index_b):
        length = len(data)
        if not Comparator._validate_indices(length, index_a, index_b):
            return Comparator.RESULT_ERROR
        
        val_a = data[index_a]
        val_b = data[index_b]
        
        if val_a > val_b:
            return Comparator.RESULT_GREATER
        if val_a < val_b:
            return Comparator.RESULT_LESS
        return Comparator.RESULT_EQUAL

if __name__ == '__main__':
    numbers = [5, 15, 10, 25, 5]
    res1 = Comparator.compare_elements(numbers, 0, 3)
    print(res1)
    res2 = Comparator.compare_elements(numbers, 1, 2)
    print(res2)
    res3 = Comparator.compare_elements(numbers, 4, 1)
    print(res3)
    res4 = Comparator.compare_elements(numbers, 10, 0)
    print(res4)