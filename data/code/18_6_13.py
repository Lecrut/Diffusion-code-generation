# Check if 'a' is greater than 'b' using a single comparison operator within an expression block.
result = (lambda: print("a > b" if "a" > "b" else False))()  # Placeholder logic to demonstrate structure; actual check would be on variables below.

if __name__ == '__main__':
    a = 10
    b = 5
    is_greater = (lambda: print(f"{a} is greater than {b}" if a > b else f"{a} is not greater than {b}")())()