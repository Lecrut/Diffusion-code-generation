from typing import List, Tuple

def generate_fibonacci(n: int) -> Tuple[List[int], List[int]]:
    if n <= 0:
        return ([], [])
    if n == 1:
        return ([0], [1])
    
    terms: List[int] = [0, 1]
    sums: List[int] = [0, 1]
    
    for i in range(2, n):
        next_val: int = terms[-1] + terms[-2]
        terms.append(next_val)
        
        current_sum: int = sums[-1] + terms[-1]
        sums.append(current_sum)
        
    return (terms, sums)

if __name__ == '__main__':
    fib_terms, fib_sums = generate_fibonacci(500)
    print(fib_terms[-1])
    print(fib_sums[-1])