def recursive_sum(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

if __name__ == '__main__':
    sample_value = 5
    result = recursive_sum(sample_value)
    print(result)