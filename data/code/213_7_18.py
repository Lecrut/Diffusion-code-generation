MAX_CHECKED_NUMBER = 10**9

def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    if n > MAX_CHECKED_NUMBER:
        raise ValueError("Number too large to check for perfect square")
    
    root = int(n ** 0.5)
    return root * root == n

if __name__ == '__main__':
    print(is_perfect_square(16))
    print(is_perfect_square(14))