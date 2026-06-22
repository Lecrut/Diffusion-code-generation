def sum_sequence(n):
    return sum(i for i in range(1, n+1))

if __name__ == '__main__':
    print(sum_sequence(10))