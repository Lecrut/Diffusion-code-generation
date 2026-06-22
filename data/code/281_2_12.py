def sum_five_integers(a, b, c, d, e):
    if not all(isinstance(x, int) and -1000 <= x <= 1000 for x in [a, b, c, d, e]):
        raise ValueError("All inputs must be integers within the range -1000 to 1000")
    
    total = 0
    for num in [a, b, c, d, e]:
        total += num
    
    return total

if __name__ == '__main__':
    result = sum_five_integers(10, 25, 30, 45, -5)
    print(result)