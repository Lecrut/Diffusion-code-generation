def maximum_of_three(a, b, c):
    return max(*[a, b, c])

if __name__ == '__main__':
    print(maximum_of_three(10, 20, 15))