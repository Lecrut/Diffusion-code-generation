def pyramid_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        prev = pyramid_triangle(n - 1)
        last_row = prev[-1]
        new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
        return prev + [new_row]

if __name__ == '__main__':
    print(pyramid_triangle(5))