def find_max_of_three(a, b, c):
    return max(*[a, b, c])

if __name__ == '__main__':
    x = 10
    y = 25
    z = 18
    result = find_max_of_three(x, y, z)
    print(result)