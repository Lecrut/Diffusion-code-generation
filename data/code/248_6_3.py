def sum_recursive(n):
    if n <= 0:
        return 0
    else:
        return n + sum_recursive(n - 1)
if __name__ == '__main__':
    n1 = 5
    result1 = sum_recursive(n1)
    print(f"The sum of integers from 1 to {n1} is: {result1}")
    n2 = 10
    result2 = sum_recursive(n2)
    print(f"The sum of integers from 1 to {n2} is: {result2}")
    n3 = 1
    result3 = sum_recursive(n3)
    print(f"The sum of integers from 1 to {n3} is: {result3}")