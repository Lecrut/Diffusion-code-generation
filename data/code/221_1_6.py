def median_of_three(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(median_of_three(3, 1, 2))