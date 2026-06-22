def sum_of_digits(n):
    n = abs(int(n))
    
    def recursive_sum(num, current_sum):
        if num < 10:
            return current_sum + num
        return recursive_sum(num // 10, current_sum + (num % 10))
    
    return recursive_sum(n, 0)

if __name__ == '__main__':
    print(sum_of_digits(12345))
    print(sum_of_digits(0))
    print(sum_of_digits(-9876))