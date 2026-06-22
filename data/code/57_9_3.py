def get_fibonacci_numbers(count: int = 75) -> list:
    if count <= 0:
        return []
    if count == 1:
        return [0]
    
    result = [0] * count
    result[0] = 0
    result[1] = 1
    
    for i in range(2, count):
        result[i] = result[i - 1] + result[i - 2]
        
    return result

if __name__ == '__main__':
    fibs = get_fibonacci_numbers()
    print(fibs)