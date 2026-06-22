FIB_START = 0
FIB_SECOND = 1

def _validate_count(n):
    if not isinstance(n, int):
        return []
    if n <= 0:
        return []
    return n

def generate_fibonacci(n):
    valid_n = _validate_count(n)
    if valid_n == 0:
        return []
    if valid_n == 1:
        return [FIB_START]
    
    sequence = [FIB_START, FIB_SECOND]
    left = FIB_START
    right = FIB_SECOND
    
    for _ in range(2, valid_n):
        current_sum = left + right
        sequence.append(current_sum)
        left = right
        right = current_sum
        
    return sequence

if __name__ == '__main__':
    terms = generate_fibonacci(100)
    print(terms)