import math
def sum_of_n_natural_numbers(n):
    return n * (n + 1) // 2
if __name__ == '__main__':
    n1 = 10
    result1 = sum_of_n_natural_numbers(n1)
    print(f"The sum of the first {n1} natural numbers is: {result1}")
    n2 = 100
    result2 = sum_of_n_natural_numbers(n2)
    print(f"The sum of the first {n2} natural numbers is: {result2}")
    n3 = 1000
    result3 = sum_of_n_natural_numbers(n3)
    print(f"The sum of the first {n3} natural numbers is: {result3}")