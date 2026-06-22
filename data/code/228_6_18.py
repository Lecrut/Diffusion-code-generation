def print_pyramid(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    def helper(k, max_width):
        if k > max_width:
            return
        print(' ' * (max_width - k) + '*' * (2 * k - 1))
        helper(k + 1, max_width)
    
    helper(1, n)

if __name__ == '__main__':
    try:
        base = 5
        print_pyramid(base)
    except ValueError as e:
        print(e)