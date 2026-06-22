def find_max_of_three(a, b, c):
    return max(*[a, b, c])

if __name__ == '__main__':
    result = find_max_of_three(10, 25, 5)
    print(result)