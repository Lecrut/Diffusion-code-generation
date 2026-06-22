def fibonacci_up_to_index(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n + 1):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence

if __name__ == '__main__':
    result = fibonacci_up_to_index(1000)
    print(result[-1])