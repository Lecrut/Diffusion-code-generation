def hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    top_bottom = ['*' * n] * 2
    middle_rows = ['*' + ' ' * (n - 2) + '*'] * (n - 2)
    return top_bottom + middle_rows

if __name__ == '__main__':
    result = hollow_square(5)
    print(result)
    print("\n".join(result))