def hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    top_bottom = "*" * n
    middle = "*" + " " * (n - 2) + "*"
    return top_bottom + "\n" + ("\n" + middle).join([top_bottom] * (n - 2)) + "\n" + top_bottom if n > 1 else top_bottom

if __name__ == "__main__":
    print(hollow_square(5))