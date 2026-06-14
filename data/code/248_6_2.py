def sum_up_to_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_up_to_n(n - 1)
if __name__ == '__main__':
    n1 = 5
    result1 = sum_up_to_n(n1)
    print(f"The sum of integers from 1 to {n1} is: {result1}")
    n2 = 10
    result2 = sum_up_to_n(n2)
    print(f"The sum of integers from 1 to {n2} is: {result2}")